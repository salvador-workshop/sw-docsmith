import argparse
import os

from .picsmith.transparentize import transparentize
from .picsmith.transparentize_desat import transparentize_desat
from .picsmith.engraving import engraving
from .picsmith.black_to_colour import black_to_colour
from .picsmith.pull_ebook_images import pull_ebook_images

root_dir = os.path.join(os.path.dirname(__file__), "..", "..")
input_dir = os.path.join(root_dir, "input")
output_dir = os.path.join(root_dir, "output")

script_desc = "Performs batch processing of images and drawing files."


def process_image():
    parser = argparse.ArgumentParser(description=script_desc)
    mode_help_msgs = [
        "[ 1 ] -- Transparentize Images",
        "[ 2 ] -- Transparentize and Desaturate Images",
        "[ 3 ] -- Re-print Engravings",
        "[ 4 ] -- Convert B&W Images to Two Colours",
        "[ 5 ] -- Copy E-Book Images",
    ]
    mode_help_msg = "Available op. modes:  " + ", ".join(mode_help_msgs)
    parser.add_argument(
        "--mode",
        dest="mode",
        default=0,
        help=mode_help_msg,
    )

    args = parser.parse_args()
    input_mode = int(args.mode)

    print("\n----------------------------------------------------------------\n")

    print(f"> PROCESS IMAGE")
    print("\n----------------------------------------------------------------\n")
    print(f"> [Image Processing Mode] {input_mode}")

    if input_mode == 1:
        transparentize()
    elif input_mode == 2:
        transparentize_desat()
    elif input_mode == 3:
        engraving()
    elif input_mode == 4:
        black_to_colour()
    elif input_mode == 5:
        pull_ebook_images()
    else:
        print("> [Warning] Operation mode not recognized. No action taken.")

    print("\n----------------------------------------------------------------\n")


if __name__ == "__process_image__":
    process_image()
