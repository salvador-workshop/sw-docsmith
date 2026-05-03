from .utils import format_phone_num, format_date, sort_exp


def build_resume_full_txt(resume_info, build_opts):
    out_file_full_txt = open("build/resume-full.txt", "w", encoding="utf-8")

    # -----
    # Intro

    out_file_full_txt.write(f"{resume_info["name"].upper()}\n\n")
    out_file_full_txt.write(f"{resume_info["subtitle"].upper()}\n\n")

    # ------------
    # Contact Info

    for contact in resume_info["contact_info"]:
        copy = contact["info"].replace("https://", "")

        is_phone = contact["type"] == "phone"
        if is_phone:
            copy = format_phone_num(contact["info"])

        out_file_full_txt.write(f"{copy}  \n")
    out_file_full_txt.write("\n")

    # ------------
    # Objective

    out_file_full_txt.write(f"OBJECTIVE\n\n")
    out_file_full_txt.write(f"{resume_info["objective"]}\n\n")

    # ------------
    # Skills & Qualifications

    out_file_full_txt.write(f"SKILLS & QUALIFICATIONS\n\n")

    for skill in resume_info["skills_qualifications"]:
        out_file_full_txt.write(f"- {skill}\n")
    out_file_full_txt.write("\n")

    # ------------
    # Technical Experience

    out_file_full_txt.write(f"TECHNICAL EXPERIENCE\n\n")

    for work_exp in sorted(resume_info["work_experience"], key=sort_exp, reverse=True):
        out_file_full_txt.write(f"{work_exp["exp_role"]} — {work_exp["org_name"]}\n\n")

        start_date_str = format_date(work_exp["start_date"])
        end_date_str = (
            "Present" if not work_exp["end_date"] else format_date(work_exp["end_date"])
        )
        out_file_full_txt.write(f"{start_date_str} — {end_date_str}  \n")
        out_file_full_txt.write(f"{work_exp["org_location"]}  \n")
        out_file_full_txt.write(
            f"Core technologies — {', '.join(work_exp["skills"])}\n\n"
        )
        for highlight in work_exp["highlights"]:
            out_file_full_txt.write(f"- {highlight}\n")
        out_file_full_txt.write("\n")

    # ------------
    # Projects

    out_file_full_txt.write(f"PROJECTS\n\n")

    for proj_exp in sorted(resume_info["projects"], key=sort_exp, reverse=True):
        out_file_full_txt.write(
            f"{proj_exp["project_name"]} — {proj_exp["org_name"]}\n\n"
        )
        start_date_str = format_date(proj_exp["start_date"])
        end_date_str = (
            "Present" if not proj_exp["end_date"] else format_date(proj_exp["end_date"])
        )
        out_file_full_txt.write(f"{start_date_str} — {end_date_str}  \n")
        out_file_full_txt.write(f"{proj_exp["org_location"]}  \n")
        out_file_full_txt.write(f"Core skills — {', '.join(proj_exp["skills"])}\n\n")
        for highlight in proj_exp["highlights"]:
            out_file_full_txt.write(f"- {highlight}\n")
        out_file_full_txt.write("\n")

    # ------------
    # Technical Education

    out_file_full_txt.write(f"EDUCATION\n\n")

    for edu_exp in sorted(resume_info["education"], key=sort_exp, reverse=True):
        out_file_full_txt.write(
            f"{edu_exp["education_cred"]} — {edu_exp["org_name"]}\n\n"
        )
        start_date_str = format_date(edu_exp["start_date"])
        end_date_str = (
            "Present" if not edu_exp["end_date"] else format_date(edu_exp["end_date"])
        )
        out_file_full_txt.write(f"{start_date_str} — {end_date_str}  \n")
        out_file_full_txt.write(f"{edu_exp["org_location"]}  \n")
        out_file_full_txt.write(f"Core skills — {', '.join(edu_exp["skills"])}\n\n")
        for highlight in edu_exp["highlights"]:
            out_file_full_txt.write(f"- {highlight}\n")
        out_file_full_txt.write("\n")

    # ------------
    # Volunteering

    if "volunteering" not in build_opts["skip"]:
        out_file_full_txt.write(f"VOLUNTEERING\n\n")

        for vol_exp in sorted(resume_info["volunteering"], key=sort_exp, reverse=True):
            out_file_full_txt.write(
                f"{vol_exp["exp_role"]} — {vol_exp["org_name"]}\n\n"
            )
            start_date_str = format_date(vol_exp["start_date"])
            end_date_str = (
                "Present"
                if not vol_exp["end_date"]
                else format_date(vol_exp["end_date"])
            )
            out_file_full_txt.write(f"{start_date_str} — {end_date_str}  \n")
            out_file_full_txt.write(f"{vol_exp["org_location"]}  \n")
            out_file_full_txt.write(f"Core skills — {', '.join(vol_exp["skills"])}\n\n")
            for highlight in vol_exp["highlights"]:
                out_file_full_txt.write(f"- {highlight}\n")
            out_file_full_txt.write("\n")

    # ------------
    # About Me

    out_file_full_txt.write(f"ABOUT ME\n\n")
    out_file_full_txt.write(f"{resume_info["about"]}\n")

    # -------
    # Cleanup
    # -------

    out_file_full_txt.close()
    return 0
