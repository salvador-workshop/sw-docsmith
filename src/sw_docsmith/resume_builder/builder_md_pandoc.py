from .utils import (
    format_phone_num,
    sort_exp,
)

from .utils_md import (
    build_minimal_md_table,
    build_resume_exp_md_pandoc,
    build_minimal_row_md_table,
    format_skill_qual_md,
)


def build_resume_full_md_pandoc(resume_info, build_opts):
    out_file_full_md = open("output/resume/resume-full-pandoc.md", "w", encoding="utf-8")

    # -----
    # Intro

    out_file_full_md.write(f"# {resume_info["name"]} {{#title}}\n\n")
    out_file_full_md.write("![](src/sw_docsmith/resume_builder/icons/icon-merlion.svg \"Decorative icon (left)\")  \n")
    out_file_full_md.write("![](src/sw_docsmith/resume_builder/icons/sw-qr.svg \"QR code (right)\")\n\n")
    out_file_full_md.write(f"#### {resume_info["subtitle"]} {{#subtitle}}\n\n")

    # ------------
    # Contact Info

    num_break = 3
    contact_cells = []
    contact_cells_row_idx = -1
    for contact_idx in range(len(resume_info["contact_info"])):
        contact = resume_info["contact_info"][contact_idx]
        if contact_idx % num_break == 0:
            contact_cells.append([])
            contact_cells_row_idx += 1
        link = contact["info"]
        copy = contact["info"].replace("https://", "")
        contact_icon_src = "src/sw_docsmith/resume_builder/icons/generic.svg"

        if contact["type"] == "website":
            contact_icon_src = "src/sw_docsmith/resume_builder/icons/user-circle.svg"
        elif contact["type"] == "email":
            link = f"mailto:{contact["info"] }"
            contact_icon_src = "src/sw_docsmith/resume_builder/icons/email.svg"
        elif contact["type"] == "phone":
            link = f"tel:{format_phone_num(contact["info"], "html")}"
            copy = format_phone_num(contact["info"])
            contact_icon_src = "src/sw_docsmith/resume_builder/icons/phone.svg"
        elif contact["type"] == "github":
            copy = contact["info"].replace("https://github.com/", "")
            contact_icon_src = "src/sw_docsmith/resume_builder/icons/github.svg"
        elif contact["type"] == "linkedin":
            copy = contact["info"].replace("https://linkedin.com/in/", "")
            contact_icon_src = "src/sw_docsmith/resume_builder/icons/linkedin.svg"

        contact_alt = f"Icon ({contact["type"]})"
        contact_icon = f'![{contact_alt}]({contact_icon_src} "{contact_alt}")'
        contact_cells[contact_cells_row_idx].append(
            f"{contact_icon}&nbsp; [{copy}]({link})"
        )

    contacts_table = build_minimal_md_table(contact_cells)

    out_file_full_md.write(contacts_table)
    out_file_full_md.write("\n")

    # ------------
    # Objective

    out_file_full_md.write(f"## Objective\n\n")
    out_file_full_md.write(f"{resume_info["objective"]}\n\n")

    # ------------
    # Skills & Qualifications

    out_file_full_md.write(f"## Skills & Qualifications {{#skills-quals}}\n\n")

    skill_cells = []
    for skill in resume_info["skills_qualifications"]:
        skill_cells.append(format_skill_qual_md(skill))
    skills_table = build_minimal_row_md_table(skill_cells)
    out_file_full_md.write(skills_table)
    out_file_full_md.write("\n")

    # ------------
    # Technical Experience

    out_file_full_md.write(f"## Technical Experience\n\n")

    for work_exp in sorted(resume_info["work_experience"], key=sort_exp, reverse=True):
        build_resume_exp_md_pandoc(work_exp, out_file_full_md)

    # ------------
    # Projects

    out_file_full_md.write(f"## Projects\n\n")

    for proj_exp in sorted(resume_info["projects"], key=sort_exp, reverse=True):
        build_resume_exp_md_pandoc(proj_exp, out_file_full_md)

    # ------------
    # Technical Education

    out_file_full_md.write(f"## Education\n\n")

    for edu_exp in sorted(resume_info["education"], key=sort_exp, reverse=True):
        build_resume_exp_md_pandoc(edu_exp, out_file_full_md)

    # ------------
    # Volunteering
    if "volunteering" not in build_opts["skip"]:
        out_file_full_md.write(f"## Volunteering\n\n")

        for vol_exp in sorted(resume_info["volunteering"], key=sort_exp, reverse=True):
            build_resume_exp_md_pandoc(vol_exp, out_file_full_md)

    # ------------
    # About Me

    out_file_full_md.write(f"## About Me\n\n")
    out_file_full_md.write(f"{resume_info["about"]}\n")

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0
