#! python3

#///============================================================
#///   1 -- TRANSPARENTIZE
#///------------------------------------------------------------
#///   Makes image transparent/translucent based on lightness
#///------------------------------------------------------------

import os
from PIL import Image, ImageEnhance, ImageOps

from .utils import setup_transform, save_image, print_exception

def transparentize():

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
            

            #/////   Create img where white = transparent, write to output
            invertedImg = rgbImg.convert('L').point(lambda p: 255 - p)

            transparentImg = rgbImg.copy()
            transparentImg.putalpha(invertedImg)

            #/////   Re-saturate -- images lose a lot of colour after .putalpha()
            resat = ImageEnhance.Color(transparentImg)
            resatImg = resat.enhance(2)

            save_image(resatImg, filename, output_fname, album_output_dir, cfg_file_preserve_fname, cfg_file_slugify_fname)
        except Exception as err:
            print_exception(err, 'TRANSPARENTIZE', filename)
