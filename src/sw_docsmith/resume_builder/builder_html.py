import pandoc
from pandoc.types import *
from .utils import print_splash, format_phone_num, format_date


def build_resume_full_html(build_opts):
    markdown_data = open("output/resume/resume-full-pandoc.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    write_opts = [
        "--embed-resources",
        "--standalone",
        "--css",
        "src/sw_docsmith/resume_builder/util/resume_style.css",
        "--css",
        "src/sw_docsmith/resume_builder/util/resume_web.css",
    ]
    pandoc.write(
        doc, "output/resume/resume-full.html", format="html", options=write_opts
    )

    return 0


def build_cover_letter_html(build_opts):
    markdown_data = open("output/resume/cover-letter-pandoc.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    write_opts = [
        "--embed-resources",
        "--standalone",
        "--css",
        "src/sw_docsmith/resume_builder/util/cover_letter_style.css",
        "--css",
        "src/sw_docsmith/resume_builder/util/cover_letter_web.css",
    ]
    pandoc.write(
        doc, "output/resume/cover-letter.html", format="html", options=write_opts
    )

    return 0


def build_search_helper_html(build_opts):
    markdown_data = open("output/resume/search-helper-pandoc.md", "r", encoding="utf-8")
    doc = pandoc.read(markdown_data.read())

    write_opts = [
        "--embed-resources",
        "--standalone",
        "--include-in-header",
        "src/sw_docsmith/resume_builder/util/search_helper_copy.html",
        "--css",
        "src/sw_docsmith/resume_builder/util/search_helper_style.css",
        "--css",
        "src/sw_docsmith/resume_builder/util/search_helper_web.css",
    ]
    pandoc.write(
        doc, "output/resume/search-helper.html", format="html", options=write_opts
    )

    return 0
