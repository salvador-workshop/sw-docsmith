import argparse
import pathlib
import os

root_dir = os.path.join(os.path.dirname(__file__), "..", "..")
input_dir = os.path.join(root_dir, "input")
output_dir = os.path.join(root_dir, "output")


def transform_clean():

    parser = argparse.ArgumentParser(
        description="Transforms models in the given input project"
    )
    parser.add_argument(
        "--project",
        dest="project",
        default="!",
        help="Project directory in `input/`",
    )

    args = parser.parse_args()
    input_project = args.project or None

    input_dir_data = pathlib.Path(input_dir)
    input_dir_list = list(input_dir_data.iterdir())
    input_dir_project_dirs = list(filter(lambda item: item.is_dir(), input_dir_list))
    input_dir_projects = list(
        map(lambda path_obj: path_obj.name, input_dir_project_dirs)
    )

    if input_project not in input_dir_projects:
        raise ValueError(
            f"No project specified! System could not find a directory at `input/{input_project}`"
        )
    else:
        proj_id = input_project
        proj_model = os.path.join(input_dir, proj_id, f"{proj_id}.stl")
        proj_out_dir = os.path.join(output_dir, proj_id)
        out_model = os.path.join(proj_out_dir, f"{proj_id}-simplified.stl")

    print("----------------------------------------------------------------\n")
    print(f"> Preparing to transform models from `input/{proj_id}`...")

    print("\n----------------------------------------------------------------\n")


if __name__ == "__transform_clean__":
    transform_clean()
