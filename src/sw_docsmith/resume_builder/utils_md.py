from resume_builder.utils import (
    get_dashline,
    get_dashline_for_str,
    get_padline,
    html_newline,
    typ_tbl_char_padding,
)
from .utils import (
    format_date,
)
import re


def build_multiline_md_table(cells):
    """Builds a minimal (headless) two-dimensional table with multiline cells. Data formata: cells[rowIdx][colIdx]"""
    borders = []
    contentlines = []
    contentlines_raw = {}
    line_lengths_by_col = {}
    line_nums_by_row = {}
    highest_row_idx = 0
    highest_col_idx = 0

    # ---
    # Reading
    # ---

    for row_idx in range(len(cells)):
        contentlines_raw[row_idx] = []
        if row_idx > highest_row_idx:
            highest_row_idx = row_idx
        if row_idx not in line_nums_by_row:
            line_nums_by_row[row_idx] = []

        for col_idx in range(len(cells[row_idx])):
            if col_idx not in line_lengths_by_col:
                line_lengths_by_col[col_idx] = []
            if col_idx > highest_col_idx:
                highest_col_idx = col_idx

            contentlines_raw[row_idx].append([])
            curr_line = cells[row_idx][col_idx]

            # check the lengths of each line in the cell
            raw_lines = curr_line.splitlines()

            highest_line_idx = 0
            for line_idx in range(len(raw_lines)):
                highest_line_idx += 1
                cell_line = raw_lines[line_idx]
                line_lengths_by_col[col_idx].append(len(cell_line))
                contentlines_raw[row_idx][col_idx].append(cell_line)
            line_nums_by_row[row_idx].append(highest_line_idx)

        line_nums_by_row[row_idx] = max(line_nums_by_row[row_idx])

    # ---
    # Preparing
    # ---

    for row_idx in range(highest_col_idx + 1):
        borders.append(
            get_dashline(max(line_lengths_by_col[row_idx]) + typ_tbl_char_padding)
        )

    total_lines = 0
    for max_line_num in line_nums_by_row.values():
        total_lines += max_line_num

    for row_idx in range(len(contentlines_raw)):
        max_lines = line_nums_by_row[row_idx]

        for l_idx in range(max_lines):
            line_parts = []

            for col_idx in range(len(contentlines_raw[row_idx])):
                max_line_len = max(line_lengths_by_col[col_idx])

                try:
                    c_line = contentlines_raw[row_idx][col_idx][l_idx]
                    if (
                        len(contentlines_raw[row_idx][col_idx]) > 1
                        and l_idx != len(contentlines_raw[row_idx]) - 1
                    ):
                        c_line += html_newline
                    else:
                        c_line += get_padline("", len(html_newline))
                except IndexError:
                    c_line = ""

                c_line_part = get_padline(
                    c_line,
                    max_line_len + typ_tbl_char_padding,
                )
                line_parts.append(c_line_part)

            contentlines.append("  ".join(line_parts))

    # ---
    # Writing
    # ---

    out_strs = ["  ".join(borders)]
    out_strs.append("\n".join(contentlines))
    borderpad = ""
    if highest_row_idx == 0:
        # "It is possible for a multiline table to have just one row, but the row should
        # be followed by a blank line (and then the row of dashes that ends the table),
        # or the table may be interpreted as a simple table."
        borderpad = "\n"
    out_strs.append(borderpad + "  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str


def build_resume_exp_md(exp, openfile):
    exp_title = ""

    if exp["exp_type"] == "work":
        exp_title = format_exp_title_md(exp["exp_role"])
    elif exp["exp_type"] == "education":
        exp_title = format_exp_title_md(exp["education_cred"])
    elif exp["exp_type"] == "project":
        exp_title = format_exp_title_md(exp["project_name"])
    else:
        exp_title = format_exp_title_md(exp["exp_role"])

    openfile.write(f"### {exp_title} — _{exp["org_name"]}_ {{.exp-heading}}\n\n")

    start_date_str = format_date(exp["start_date"])
    end_date_str = "Present" if not exp["end_date"] else format_date(exp["end_date"])

    skill_header = "Core skills"
    # skill_header = "Core technologies" if exp["exp_type"] == "work" else "Core skills"
    if exp["exp_type"] == "work":
        skill_header = "Core technologies"
    elif exp["exp_type"] == "volunteering":
        skill_header = "Skills"

    cells = [
        [
            f"_**{start_date_str} — {end_date_str}**\n{exp["org_location"]}_",
            f"_**{skill_header}** — {', '.join(exp["skills"])}_",
        ]
    ]
    openfile.write(f"{build_multiline_md_table(cells)}\n")

    for highlight in exp["highlights"]:
        openfile.write(f"- {highlight}\n")
    openfile.write("\n")


def build_resume_exp_md_pandoc(exp, openfile):
    exp_title = ""

    if exp["exp_type"] == "work":
        exp_title = format_exp_title_md(exp["exp_role"])
    elif exp["exp_type"] == "education":
        exp_title = format_exp_title_md(exp["education_cred"])
    elif exp["exp_type"] == "project":
        exp_title = format_exp_title_md(exp["project_name"])
    else:
        exp_title = format_exp_title_md(exp["exp_role"])

    openfile.write(f"### {exp_title} — _{exp["org_name"]}_ {{.exp-heading}}\n\n")

    start_date_str = format_date(exp["start_date"])
    end_date_str = "Present" if not exp["end_date"] else format_date(exp["end_date"])

    skill_header = "Core skills"

    if exp["exp_type"] == "work":
        skill_header = "Core technologies"
    elif exp["exp_type"] == "volunteering":
        skill_header = "Skills"

    spacer = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    openfile.write(
        f"_**{start_date_str} — {end_date_str}** {spacer} {exp["org_location"]}_  \n"
    )
    openfile.write(f"_**{skill_header}** — {', '.join(exp["skills"])}_\n\n")

    for highlight in exp["highlights"]:
        openfile.write(f"- {highlight}\n")
    openfile.write("\n")


def build_minimal_row_md_table(cells):
    """Builds a minimal (headless) one-row table."""
    borders = []
    contentlines = []

    for cell_str in cells:
        dashline = get_dashline_for_str(cell_str)
        borders.append(dashline)
        contentlines.append(get_padline(cell_str, len(dashline)))

    out_strs = ["  ".join(borders)]
    out_strs.append("  ".join(contentlines))
    out_strs.append("  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str


def build_minimal_md_table(cells):
    """Builds a minimal (headless) two-dimensional table. Data formata: cells[rowIdx][colIdx]"""
    borders = []
    contentlines = {}
    contentlines_raw = {}
    line_lengths_by_col = {}
    highest_row_idx = 0
    highest_col_idx = 0

    # ---
    # Reading
    # ---

    for row_idx in range(len(cells)):
        contentlines_raw[row_idx] = []
        if row_idx > highest_row_idx:
            highest_row_idx = row_idx
        for col_idx in range(len(cells[row_idx])):
            if col_idx not in line_lengths_by_col:
                line_lengths_by_col[col_idx] = []
            if col_idx > highest_col_idx:
                highest_col_idx = col_idx

            curr_line = cells[row_idx][col_idx]
            contentlines_raw[row_idx].append(curr_line)
            line_lengths_by_col[col_idx].append(len(curr_line))

    # ---
    # Preparing
    # ---

    for row_idx in range(highest_col_idx + 1):
        borders.append(
            get_dashline(max(line_lengths_by_col[row_idx]) + typ_tbl_char_padding)
        )

    for row_idx in range(len(cells)):
        contentlines[row_idx] = []
        contentline_pts = []
        for col_idx in range(len(cells[row_idx])):
            max_line_len = max(line_lengths_by_col[col_idx])
            contentline_part = get_padline(
                contentlines_raw[row_idx][col_idx],
                max_line_len + typ_tbl_char_padding,
            )
            contentline_pts.append(contentline_part)
        contentlines[row_idx].append("  ".join(contentline_pts))

    # ---
    # Writing
    # ---

    out_strs = ["  ".join(borders)]
    for content_row in contentlines:
        out_strs.append("\n".join(contentlines[content_row]))
    out_strs.append("  ".join(borders))
    out_str = "\n".join(out_strs) + "\n"

    return out_str


def exp_title_md_repl(matchobj):
    return f"_{matchobj.group(0)}_"


def format_exp_title_md(str):
    out_str = re.sub(r"\((.*?)\)", exp_title_md_repl, str)
    return out_str


def format_skill_qual_md(str):
    lines = str.split("<br>")
    return f"**{lines[0]}**<br>{lines[1]}"
