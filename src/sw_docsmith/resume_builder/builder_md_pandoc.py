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

from .builder_txt import build_resume_exp_txt


def build_resume_full_md_pandoc(resume_info, build_opts):
    out_file_full_md = open(
        "output/resume/resume-full-pandoc.md", "w", encoding="utf-8"
    )

    # -----
    # Intro

    out_file_full_md.write(f"# {resume_info["name"]} {{#title}}\n\n")
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/icon-merlion.svg "Decorative icon (left)")  \n'
    )
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/sw-qr.svg "QR code (right)")\n\n'
    )
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


def build_cover_letter_md_pandoc(complete_resume_info, build_opts):
    resume_info = complete_resume_info["resume"]
    cover_info = complete_resume_info["cover"]
    contact_info = resume_info["contact_info"]

    contact_email = [x for x in contact_info if x["type"] == "email"][0]
    contact_phone = [x for x in contact_info if x["type"] == "phone"][0]
    contact_website = [x for x in contact_info if x["type"] == "website"][0]
    contact_github = [x for x in contact_info if x["type"] == "github"][1]
    contact_linkedin = [x for x in contact_info if x["type"] == "linkedin"][0]

    out_file_full_md = open(
        "output/resume/cover-letter-pandoc.md", "w", encoding="utf-8"
    )

    # ------------
    # Heading, Intro

    out_file_full_md.write(f"# {resume_info["name"]} {{#title}}\n\n")
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/icon-shell.svg "Decorative icon (left)")  \n'
    )
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/sw-qr.svg "QR code (right)")\n\n'
    )
    out_file_full_md.write(f"#### Cover Letter {{#subtitle}}\n")
    out_file_full_md.write(f"\n")

    out_file_full_md.write(f"{cover_info["greeting"]}\n")
    out_file_full_md.write(f"\n")

    out_file_full_md.write(f"{cover_info["career_objective"]}\n")
    out_file_full_md.write(f"\n")

    # ------------
    # Body

    for rel_exp in cover_info["relevant_experience"]:
        out_file_full_md.write(f"{rel_exp} ")

    out_file_full_md.write(f"\n\n")

    out_file_full_md.write(f"{cover_info["closing"]}\n")
    out_file_full_md.write(f"\n")

    # ------------
    # Contact

    out_file_full_md.write(f"{cover_info["signoff"]},  \n")
    out_file_full_md.write(f"<br/>\n")

    out_file_full_md.write(f"**{resume_info["name"]}**  \n")
    out_file_full_md.write(
        f"[{contact_email['info']}](mailto:{contact_email['info']})  \n"
    )
    out_file_full_md.write(
        f"[{format_phone_num(contact_phone['info'])}](tel:{format_phone_num(contact_phone['info'], "html")})  \n"
    )

    out_file_full_md.write(f"<br/>\n")

    out_file_full_md.write(
        f"[{contact_website['info']}]({contact_website['info']})  \n"
    )
    out_file_full_md.write(f"[{contact_github['info']}]({contact_github['info']})  \n")
    out_file_full_md.write(
        f"[{contact_linkedin['info']}]({contact_linkedin['info']})  \n"
    )

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0


def build_search_helper_md_pandoc(complete_resume_info, build_opts):
    resume_info = complete_resume_info["resume"]
    cover_info = complete_resume_info["cover"]
    contact_info = resume_info["contact_info"]

    contact_email = [x for x in contact_info if x["type"] == "email"][0]
    contact_phone = [x for x in contact_info if x["type"] == "phone"][0]
    contact_website = [x for x in contact_info if x["type"] == "website"][0]
    contact_github = [x for x in contact_info if x["type"] == "github"][1]
    contact_linkedin = [x for x in contact_info if x["type"] == "linkedin"][0]

    out_file_full_md = open(
        "output/resume/search-helper-pandoc.md", "w", encoding="utf-8"
    )

    # ------------
    # Heading, Intro

    out_file_full_md.write(f"# {resume_info["name"]} {{#title}}\n\n")
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/icon-shell.svg "Decorative icon (left)")  \n'
    )
    out_file_full_md.write(
        '![](src/sw_docsmith/resume_builder/icons/icon-merlion.svg "Decorative icon (right)")  \n\n'
    )
    out_file_full_md.write(f"#### Job Search Helper {{#subtitle}}\n")
    out_file_full_md.write(f"\n")

    # -------
    # Data Setup
    # -------

    contact_data = []
    for contact_ctg in contact_info:
        print("contact_ctg")
        new_contact_data = {
            "id": f"contact.{contact_ctg['type']}",
            "value": contact_ctg["info"],
        }
        print(new_contact_data)
        contact_data.append(new_contact_data)

    resume_data = []
    for resume_ctg in resume_info:
        print("resume_ctg")
        resume_val = resume_info[resume_ctg]
        if resume_ctg != "contact_info":
            if isinstance(resume_val, list):
                for idx, resume_exp_data in enumerate(resume_val):
                    if resume_ctg == "skills_qualifications":
                        resume_exp_entry = resume_exp_data
                        new_resume_data = {
                            "id": f"resume.{resume_ctg}.{idx + 1}",
                            "value": resume_exp_entry,
                        }
                        print(new_resume_data)
                        resume_data.append(new_resume_data)
                    else:
                        resume_exp_entry = build_resume_exp_txt(resume_exp_data)
                        new_resume_data = {
                            "id": f"resume.{resume_ctg}.{idx + 1}",
                            "value": resume_exp_entry,
                        }
                        print(new_resume_data)
                        resume_data.append(new_resume_data)
            else:
                new_resume_data = {
                    "id": f"resume.{resume_ctg}",
                    "value": resume_val,
                }
                print(new_resume_data)
                resume_data.append(new_resume_data)

    cover_data = []
    for cover_ctg in cover_info:
        cover_val = cover_info[cover_ctg]
        print("cover_ctg")
        if isinstance(cover_val, list):
            for idx, cover_detail_data in enumerate(cover_val):
                new_cover_data = {
                    "id": f"cover.{cover_ctg}.{idx + 1}",
                    "value": cover_detail_data,
                }
                print(new_cover_data)
                cover_data.append(new_cover_data)
        else:
            new_cover_data = {
                "id": f"cover.{cover_ctg}",
                "value": cover_val,
            }
            print(new_cover_data)
            cover_data.append(new_cover_data)

    # -------
    # Data Writing
    # -------
    out_file_full_md.write(f"\n")

    out_file_full_md.write(f"---\n")
    out_file_full_md.write(
        f"header-includes: <script>const copyIt = (keyStr) => {{console.log(keyStr)}}</script>\n"
    )
    out_file_full_md.write(f"---\n")

    for contact_details in contact_data:
        out_file_full_md.write(f"### {contact_details['id']} {{.data-heading}}\n")
        out_file_full_md.write(
            f"<button onClick=\"copyIt('{contact_details['id']}')\">Copy text</button>"
        )
        out_file_full_md.write(f"\n")
        out_file_full_md.write(f"```\n{contact_details['value']}\n```\n")
        out_file_full_md.write(f"\n")

    for resume_details in resume_data:
        out_file_full_md.write(f"### {resume_details['id']} {{.data-heading}}\n")
        out_file_full_md.write(
            f"<button onClick=\"copyIt('{resume_details['id']}')\">Copy text</button>"
        )
        out_file_full_md.write(f"\n")
        out_file_full_md.write(f"```\n{resume_details['value']}\n```\n")
        out_file_full_md.write(f"\n")

    for cover_details in cover_data:
        out_file_full_md.write(f"### {cover_details['id']} {{.data-heading}}\n")
        out_file_full_md.write(
            f"<button onClick=\"copyIt('{cover_details['id']}')\">Copy text</button>"
        )
        out_file_full_md.write(f"\n")
        out_file_full_md.write(f"```\n{cover_details['value']}\n```\n")
        out_file_full_md.write(f"\n")

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0
