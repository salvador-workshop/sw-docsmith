#! python3

#///============================================================
#///   3 -- ENGRAVING
#///------------------------------------------------------------
#///   Desaturates images, and reduces values to (mostly) black
#///   and white
#///------------------------------------------------------------

import os, math
from PIL import Image, ImageEnhance, ImageOps

from .utils import setup_transform, save_image, print_exception

def engraving():

    #///////////////////////////////////////////////////////////////////////
    #/////   MATHEMATICS   /////////////////////////////////////////////////

    # ideal sigmoid base function:
    # f(0) = almost 0
    # f(0.5) = 0.5
    # f(1.0) = almost 1.0

    # sigmoidBaseCoeff controls the curve of the function. Lower values
    # make a gentler curve from 0.5 to either extreme. Higher values make
    # that curve steep, and reaches either extreme value more easily
    sigmoidBaseCoeff = 200
    # this sigmoid func works for values between 0 and 1
    sigmoidBase = lambda x: 1 / (1 + math.exp(-(x-0.5) * sigmoidBaseCoeff))

    # sigmoid function modified for values between 0 and 255 (both incl.)
    sigMax = 256
    sigMid = sigMax / 2
    # sig256Coeff = 0.125
    sig256Coeff = 0.075
    # sig256Coeff = 0.88
    # sig256Coeff = 4
    sigmoid256 = lambda x: 1 / (1 + math.exp(-(x - sigMid) * sig256Coeff)) * sigMax

    def convertBlackAndWhite(x):
        sigVal = sigmoid256(x)
        outVal = sigVal

        white_threshold = 255 * 0.6
        black_threshold = 255 * 0.125

        if sigVal > white_threshold:
            outVal = 255
        elif sigVal > black_threshold:
            outVal = 0

        return sigVal

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
            
            #/////   Desaturate
            desat = ImageEnhance.Color(rgbImg)
            greyscaleImage = desat.enhance(0)
            
            #/////   Increase contrast and brightness
            contrast = ImageEnhance.Contrast(greyscaleImage)
            contrastImg = contrast.enhance(1.25)

            brightness = ImageEnhance.Brightness(contrastImg)
            # brightImg = brightness.enhance(1.1)
            brightImg = brightness.enhance(0.92)

            #/////   Flatten colours to mostly black and white, write as thumbnail
            bwImg = contrastImg.point(convertBlackAndWhite)
            save_image(bwImg, filename, output_fname, album_output_dir, cfg_file_preserve_fname, cfg_file_slugify_fname)
        except Exception as err:
            print_exception(err, 'RE-ENGRAVING', filename)
