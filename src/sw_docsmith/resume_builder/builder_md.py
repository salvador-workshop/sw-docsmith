from .utils import format_phone_num, format_date, sort_exp


def build_resume_full_md(resume_info, build_opts):
    out_file_full_md = open("build/resume-full.md", "w", encoding="utf-8")

    # -----
    # Intro

    out_file_full_md.write(f"# {resume_info["name"]}\n\n")
    out_file_full_md.write(f"### {resume_info["subtitle"]}\n\n")

    # ------------
    # Contact Info

    for contact in resume_info["contact_info"]:
        link = contact["info"]
        copy = contact["info"].replace("https://", "")
        if contact["type"] == "email":
            link = f"mailto:{contact["info"] }"
        elif contact["type"] == "phone":
            link = f"tel:{format_phone_num(contact["info"], "html")}"
            copy = format_phone_num(contact["info"])
        elif contact["type"] == "github":
            copy = contact["info"].replace("https://", "")
        elif contact["type"] == "linkedin":
            copy = contact["info"].replace("https://", "")

        out_file_full_md.write(f"[{copy}]({link})  \n")
    out_file_full_md.write("\n")

    # ------------
    # Objective

    out_file_full_md.write(f"## Objective\n\n")
    out_file_full_md.write(f"{resume_info["objective"]}\n\n")

    # ------------
    # Skills & Qualifications

    out_file_full_md.write(f"## Skills & Qualifications\n\n")

    for skill in resume_info["skills_qualifications"]:
        out_file_full_md.write(f"{skill}\n\n")
    out_file_full_md.write("\n")

    # ------------
    # Technical Experience

    out_file_full_md.write(f"## Technical Experience\n\n")

    for work_exp in sorted(resume_info["work_experience"], key=sort_exp, reverse=True):
        out_file_full_md.write(
            f"### {work_exp["exp_role"]} — _{work_exp["org_name"]}_\n\n"
        )

        start_date_str = format_date(work_exp["start_date"])
        end_date_str = (
            "Present" if not work_exp["end_date"] else format_date(work_exp["end_date"])
        )
        out_file_full_md.write(
            f"**{start_date_str} — {end_date_str}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {work_exp["org_location"]}  \n"
        )
        out_file_full_md.write(
            f"**Key technologies** — {', '.join(work_exp["skills"])}\n\n"
        )
        for highlight in work_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # Projects

    out_file_full_md.write(f"## Projects\n\n")

    for proj_exp in sorted(resume_info["projects"], key=sort_exp, reverse=True):
        out_file_full_md.write(
            f"### {proj_exp["project_name"]} — _{proj_exp["org_name"]}_\n\n"
        )
        start_date_str = format_date(proj_exp["start_date"])
        end_date_str = (
            "Present" if not proj_exp["end_date"] else format_date(proj_exp["end_date"])
        )
        out_file_full_md.write(
            f"**{start_date_str} — {end_date_str}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {proj_exp["org_location"]}  \n"
        )
        out_file_full_md.write(f"**Key skills** — {', '.join(proj_exp["skills"])}\n\n")
        for highlight in proj_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # Technical Education

    out_file_full_md.write(f"## Education\n\n")

    for edu_exp in sorted(resume_info["education"], key=sort_exp, reverse=True):
        out_file_full_md.write(
            f"### {edu_exp["education_cred"]} — _{edu_exp["org_name"]}_\n\n"
        )
        start_date_str = format_date(edu_exp["start_date"])
        end_date_str = (
            "Present" if not edu_exp["end_date"] else format_date(edu_exp["end_date"])
        )
        out_file_full_md.write(
            f"**{start_date_str} — {end_date_str}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {edu_exp["org_location"]}  \n"
        )
        out_file_full_md.write(f"**Key skills** — {', '.join(edu_exp["skills"])}\n\n")
        for highlight in edu_exp["highlights"]:
            out_file_full_md.write(f"- {highlight}\n")
        out_file_full_md.write("\n")

    # ------------
    # Volunteering
    if "volunteering" not in build_opts["skip"]:
        out_file_full_md.write(f"## Volunteering\n\n")

        for vol_exp in sorted(resume_info["volunteering"], key=sort_exp, reverse=True):
            out_file_full_md.write(f"### {vol_exp["exp_role"]} — _{vol_exp["org_name"]}_\n\n")
            start_date_str = format_date(vol_exp["start_date"])
            end_date_str = (
                "Present" if not vol_exp["end_date"] else format_date(vol_exp["end_date"])
            )
            out_file_full_md.write(
                f"**{start_date_str} — {end_date_str}** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {vol_exp["org_location"]}  \n"
            )
            out_file_full_md.write(f"**Key skills** — {', '.join(vol_exp["skills"])}\n\n")
            for highlight in vol_exp["highlights"]:
                out_file_full_md.write(f"- {highlight}\n")
            out_file_full_md.write("\n")

    # ------------
    # About Me

    out_file_full_md.write(f"## About Me\n\n")
    out_file_full_md.write(f"{resume_info["about"]}\n")

    # -------
    # Cleanup
    # -------

    out_file_full_md.close()
    return 0
