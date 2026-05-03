import pandoc
from pandoc.types import *
from .utils import print_splash, format_phone_num, format_date


def build_resume_full_html(build_opts):
    markdown_data = open("build/resume-full-pandoc.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    write_opts = [
        "--embed-resources",
        "--standalone",
        "--css",
        "src/resume_builder/util/resume_style.css",
        "--css",
        "src/resume_builder/util/resume_web.css",
    ]
    pandoc.write(doc, "build/resume-full.html", format="html", options=write_opts)

    return 0
