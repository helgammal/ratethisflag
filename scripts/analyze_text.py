# OCR results:

# (flags) hamdys-mbp:flags helgammal$ ls -1 textless_flags/ | wc -l
#       57
# (flags) hamdys-mbp:flags helgammal$ ls -1 textful_flags/ | wc -l
#       25
# Filtering the OCR results, the true picture appears...
# (flags) hamdys-mbp:flags helgammal$ ls -1 textful_flags/ | wc -l
#       55
# (flags) hamdys-mbp:flags helgammal$ ls -1 textless_flags/ | wc -l
#       27
# OCR thought 30 flags were textless -- they just had some curved text or 
# had bad resolution flags and were really textful.

# Conclusion: About 67% of available U.S. city flags available through Wikimedia
# have text in them (!)

try:
    from PIL import Image
except ImportError:
    import Image
import os

import shutil
import sys

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def ocr_image(image_path):
    return pytesseract.image_to_string(Image.open(image_path))

images_path = sys.argv[1]
path_format = '/Users/helgammal/lightning_talks/flags/images/{0}'
textless = '/Users/helgammal/lightning_talks/flags/textless_flags'
textful = '/Users/helgammal/lightning_talks/flags/textful_flags'
image_texts = {}

with open(images_path,'r') as f:
    for name in f.readlines():
        curr_path = path_format.format(name).strip()
        ocr_result = ocr_image(curr_path)
        image_texts[curr_path] = ocr_result.replace('\n',
                        '').replace('\r','').replace(' ','')

for key,value in image_texts.items():
    if value == '':
        shutil.copy(key,textless)
    else:
        shutil.copy(key,textful)