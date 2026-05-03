import argparse
import os

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
    mode_help_msg =  "Available op. modes:  " + ", ".join(mode_help_msgs)
    parser.add_argument(
        "--mode",
        dest="mode",
        default=None,
        help=mode_help_msg,
    )

    args = parser.parse_args()
    input_mode = args.mode

    print("\n----------------------------------------------------------------\n")

    print(f"> Test content")
    print(f"> Image Processing Mode: {input_mode}")

    print("\n----------------------------------------------------------------\n")


if __name__ == "__process_image__":
    process_image()
