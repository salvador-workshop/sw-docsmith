import pandoc
from pandoc.types import *
from .utils import print_splash, format_phone_num, format_date


def build_resume_full_pdf(build_opts):
    markdown_data = open("build/resume-full-pandoc.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    weasyprint_opts = "-e utf8 -p --hinting"
    write_opts = [
        "--css",
        "src/resume_builder/util/resume_style.css",
        "--css",
        "src/resume_builder/util/resume_print.css",
        "--to",
        "html",
        "--pdf-engine-opt",
        weasyprint_opts,
    ]
    pandoc.write(doc, "build/resume-full.pdf", format="pdf", options=write_opts)

    return 0
