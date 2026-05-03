import json


def parse_resume():
    # -------------
    # LOADING FILES
    # -------------

    resume_data = open("data/resume.json", "r", encoding="utf-8")
    contacts_data = open("data/contacts.json", "r", encoding="utf-8")
    experience_data = open("data/experience.json", "r", encoding="utf-8")
    cover_data = open("data/cover.json", "r", encoding="utf-8")

    # print(resume_data)

    resume_info = json.load(resume_data)
    contacts_info = json.load(contacts_data)
    experience_info = json.load(experience_data)
    cover_info = json.load(cover_data)

    # print(resume_info)

    # ---------------
    # DEFINITIONS
    # ---------------

    modes = {
        "full": {"desc": "Full resume (2 pg max)"},
        "short": {"desc": "Compact resume (1 pg max)"},
        "tiny": {"desc": "Very compact summary (150 char max)"},
        "cover": {"desc": "Cover letter"},
    }

    complete_resume_info = {
        "resume": {
            "contact_info": contacts_info["contacts"],
            "work_experience": experience_info["work_experience"],
            "education": experience_info["education"],
            "projects": experience_info["projects"],
            "volunteering": experience_info["volunteering"],
        },
        "cover": cover_info,
    }
    complete_resume_info["resume"].update(resume_info)

    # print(complete_resume_info)

    return complete_resume_info
