#! python3

#///============================================================
#///   4 -- BLACK TO COLOUR
#///------------------------------------------------------------
#///   Changes hues in an image based on darkness
#///------------------------------------------------------------

import os
from PIL import Image, ImageEnhance, ImageColor

from .utils import setup_transform, save_image, print_exception

def black_to_colour():

    #///////////////////////////////////////////////////////////////////////
    #/////   SETUP   ///////////////////////////////////////////////////////

    setup_data = setup_transform()

    current_dir = setup_data['current_dir']
    input_dir = setup_data['input_dir']
    output_dir = setup_data['output_dir']

    cfg_file_preserve_fname = setup_data['cfg_file_preserve_fname']
    cfg_file_slugify_fname = setup_data['cfg_file_slugify_fname']
    cfg_file_prefix = setup_data['cfg_file_prefix']
    cfg_file_count_start = setup_data['cfg_file_count_start']
    cfg_colour_fg = setup_data['cfg_colour_fg']
    cfg_colour_bg = setup_data['cfg_colour_bg']

    datestamp = setup_data['datestamp']
    album_dir_name = setup_data['album_dir_name']
    album_output_dir = setup_data['album_output_dir']


    print(f'Images will be saved in "{album_output_dir}"\n')

    #///////////////////////////////////////////////////////////////////////
    #/////   MAIN LOOP   ///////////////////////////////////////////////////

    for idx, filename in enumerate(os.listdir(input_dir)):
        try:
            fName, fExtension = os.path.splitext(filename)
            if not (fExtension.lower() == '.png' or fExtension.lower() == '.jpg' or fExtension.lower() == '.jpeg'):
                #/////   Skip non-image files
                continue
            
            output_fname = f'{cfg_file_prefix}-{idx + cfg_file_count_start}.png'
            currentImage = Image.open(os.path.join(input_dir, filename))
            rgbImg = currentImage.convert('RGB')
            
            #/////   Desaturate
            desat = ImageEnhance.Color(rgbImg)
            greyscaleImage = desat.enhance(0)
            
            #/////   Invert, create mask
            invertedImg = greyscaleImage.point(lambda p: 255 - p).convert('L')

            themeCol = ImageColor.getrgb(cfg_colour_fg)

            colImg = Image.new('RGB', currentImage.size, themeCol)
            outputImg = Image.new('RGB', currentImage.size, ImageColor.getrgb(cfg_colour_bg))
            outputImg.paste(colImg, (0, 0), invertedImg)

            save_image(outputImg, filename, output_fname, album_output_dir, cfg_file_preserve_fname, cfg_file_slugify_fname)
        except Exception as err:
            print_exception(err, 'CONVERTING B&W TO COLOURS', filename)
