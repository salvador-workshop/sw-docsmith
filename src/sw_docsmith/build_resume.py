import argparse
import os
from .resume_builder import resume_parser, resume_builder
from pathlib import Path

root_dir = os.path.join(os.path.dirname(__file__), "..", "..")
input_dir = os.path.join(root_dir, "input")
output_dir = os.path.join(root_dir, "output")

script_desc = "Transforms models in the given input project"


def build_resume():

    parser = argparse.ArgumentParser(description=script_desc)
    args = parser.parse_args()

    print("\n----------------------------------------------------------------\n")

    print(f"> BUILDING RESUME")

    Path('output/resume').mkdir(parents=True, exist_ok=True)
    Path('output/img').mkdir(parents=True, exist_ok=True)

    resume_info = resume_parser.parse_resume()
    resume_builder.build_resume_full(resume_info)
    resume_builder.build_cover_letter(resume_info)

    print("\n----------------------------------------------------------------\n")


if __name__ == "__build_resume__":
    build_resume()
