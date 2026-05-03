# /////   Functionality used by several PicSmith transforms

import os, math, json, time, re
from datetime import datetime


def setup_transform():
    # /////   Important file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_dir = os.path.join(current_dir, "../../..")

    input_base = os.path.join(repo_dir, "input")
    input_dir = os.path.join(input_base, "img")
    input_ebook_dir = os.path.join(input_base, "ebook")

    output_dir = os.path.join(repo_dir, "output")
    output_img_dir = os.path.join(output_dir, "img")
    output_ebook_dir = os.path.join(output_dir, "ebook")

    # /////   Loading configuration
    # TODO -- define default values
    with open(os.path.join(repo_dir, "config.json")) as f:
        config_data = json.load(f)

    cfg_file_preserve_fname = config_data["output"]["preserveFileName"]
    cfg_file_slugify_fname = config_data["output"]["slugifyFileName"]
    cfg_file_prefix = config_data["output"]["filePrefix"]
    cfg_file_count_start = config_data["output"]["fileCountStart"]
    cfg_colour_fg = config_data["blackToColour"]["foregroundColour"]
    cfg_colour_bg = config_data["blackToColour"]["backgroundColour"]

    epoch_time = int(time.time())
    datestamp = hex(epoch_time)
    album_dir_name = f"{cfg_file_prefix}-{datestamp}"
    album_output_dir = os.path.join(output_dir, album_dir_name)

    # /////   Creating directories, if needed
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    if not os.path.exists(input_ebook_dir):
        os.makedirs(input_ebook_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(album_output_dir):
        os.mkdir(album_output_dir)

    setup_data = {}
    setup_data["current_dir"] = current_dir
    setup_data["input_dir"] = input_dir
    setup_data["input_ebook_dir"] = input_ebook_dir
    setup_data["output_dir"] = output_dir

    setup_data["cfg_file_preserve_fname"] = cfg_file_preserve_fname
    setup_data["cfg_file_slugify_fname"] = cfg_file_slugify_fname
    setup_data["cfg_file_prefix"] = cfg_file_prefix
    setup_data["cfg_file_count_start"] = cfg_file_count_start
    setup_data["cfg_colour_fg"] = cfg_colour_fg
    setup_data["cfg_colour_bg"] = cfg_colour_bg

    setup_data["datestamp"] = datestamp
    setup_data["album_dir_name"] = album_dir_name
    setup_data["album_output_dir"] = album_output_dir

    return setup_data


def sw_slugify(input_str):
    slugged_filename = input_str.lower()
    # Remove all non-word characters (everything except numbers and letters)
    slugged_filename = re.sub(r"[^\w\s]", "", slugged_filename)
    # Replace all runs of whitespace with a single dash
    slugged_filename = re.sub(r"\s+", "-", slugged_filename)
    return slugged_filename


def save_image(
    pillow_img, orig_filename, gen_filename, output_dir, use_orig=False, slugify=False
):
    final_filename = gen_filename
    if use_orig:
        fName, fExtension = os.path.splitext(orig_filename)
        final_filename = f"{fName}.png"
    elif slugify:
        fName, fExtension = os.path.splitext(orig_filename)
        final_filename = f"{sw_slugify(fName)}.png"

    print(f'-- Converting "{orig_filename} to "{final_filename}"')
    pillow_img.save(os.path.join(output_dir, final_filename), format="png")


def print_exception(exception, operation_name, filename):
    print("---------------------------------------------------------------")
    print(f'{operation_name} on "{filename}"')
    print("FAILED DUE TO:")
    print(exception)
