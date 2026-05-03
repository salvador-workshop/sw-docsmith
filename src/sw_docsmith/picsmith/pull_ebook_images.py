#! python3

#///============================================================
#///   5 -- E-BOOK IMAGES
#///------------------------------------------------------------
#///   Pulls all images from an input e-book
#///------------------------------------------------------------

# import os, io, zipfile
import os, io
import ebooklib
from PIL import Image, ImageEnhance, ImageOps
from ebooklib import epub

from .utils import setup_transform, save_image, sw_slugify, print_exception

def pull_ebook_images():

    #///////////////////////////////////////////////////////////////////////
    #/////   SETUP   ///////////////////////////////////////////////////////

    setup_data = setup_transform()

    current_dir = setup_data['current_dir']
    ebook_input_dir = setup_data['ebook_input_dir']
    output_dir = setup_data['output_dir']

    cfg_file_preserve_fname = setup_data['cfg_file_preserve_fname']
    cfg_file_slugify_fname = setup_data['cfg_file_slugify_fname']
    cfg_file_prefix = setup_data['cfg_file_prefix']
    cfg_file_count_start = setup_data['cfg_file_count_start']

    datestamp = setup_data['datestamp']

    #///////////////////////////////////////////////////////////////////////
    #/////   MAIN LOOP   ///////////////////////////////////////////////////

    for idx, filename in enumerate(os.listdir(ebook_input_dir)):
        try:
            fName, fExtension = os.path.splitext(filename)
            if not fExtension.lower() == '.epub':
                #/////   Skip non-epub files
                continue

            # TODO -- Wrap this entire thing in a try block.
            # Make sure that if it fails, the next book will be processed
            # instead of this whole app just choking and dying
            
            file_path = os.path.join(ebook_input_dir, filename)
            print(f'Finding all images from "{filename}"...')
            # print(file_path)

            book = epub.read_epub(file_path)
            book_images = book.get_items_of_type(ebooklib.ITEM_IMAGE)
            # print(book)
            # print(book_images)

            inner_idx = 0

            default_dir_name = setup_data['album_dir_name']
            album_dir_name = f'{default_dir_name}-{idx}'
            if cfg_file_preserve_fname:
                max_fname_len = 128
                stripped_filename = fName.strip()
                truncated_name = (stripped_filename[:max_fname_len]) if len(stripped_filename) > max_fname_len else stripped_filename
                album_dir_name = f'{truncated_name}-{datestamp}'
            elif cfg_file_slugify_fname:
                max_fname_len = 128
                stripped_filename = fName.strip()
                truncated_name = (stripped_filename[:max_fname_len]) if len(stripped_filename) > max_fname_len else stripped_filename
                album_dir_name = f'{sw_slugify(truncated_name)}-{datestamp}'
            album_output_dir = os.path.join(output_dir, album_dir_name)
            if not os.path.exists(album_output_dir):
                os.makedirs(album_output_dir)

            print(f'Images will be saved in "{album_output_dir}"\n',)

            for inner_img in book_images:
                image_raw = inner_img.get_content()
                dataEnc = io.BytesIO(image_raw)
                img = Image.open(dataEnc)
                
                max_fname_len = 30
                stripped_filename = fName.strip()
                truncated_name = (stripped_filename[:max_fname_len]) if len(stripped_filename) > max_fname_len else stripped_filename

                orig_fname = f'{truncated_name}-{inner_idx}.png'
                output_fname = f'{inner_idx}.png'

                save_image(img, orig_fname, output_fname, album_output_dir, cfg_file_preserve_fname, cfg_file_slugify_fname)
                inner_idx += 1
        except Exception as err:
            print_exception(err, 'PULLING EBOOK IMAGES', filename)
