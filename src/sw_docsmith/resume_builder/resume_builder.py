import json

# from .resume_builder_utils import print_splash
from . import (
    builder_html,
    builder_md,
    builder_md_pandoc,
    builder_pdf,
    builder_txt,
)

build_opts_all = {
    "skip": []
}

build_opts = {
    "skip": ["volunteering"]
}

def build_resume_full(complete_resume_info):
    builder_txt.build_resume_full_txt(complete_resume_info["resume"], build_opts)
    # the HTML builder uses the markdown file as its data source
    builder_md.build_resume_full_md(complete_resume_info["resume"], build_opts_all)
    builder_md_pandoc.build_resume_full_md_pandoc(complete_resume_info["resume"], build_opts)
    builder_html.build_resume_full_html(build_opts)
    builder_pdf.build_resume_full_pdf(build_opts)

    return 0


def build_resume_short(complete_resume_info):
    out_file_short = open("output/resume/resume-short.txt", "w", encoding="utf-8")

    return 0


def build_resume_tiny(complete_resume_info):
    out_file_tiny = open("output/resume/resume-tiny.txt", "w", encoding="utf-8")

    return 0


def build_cover_letter(complete_resume_info):
    builder_md_pandoc.build_cover_letter_md_pandoc(complete_resume_info["resume"], build_opts)
    builder_html.build_cover_letter_html(build_opts)
    builder_pdf.build_cover_letter_pdf(build_opts)

    return 0
