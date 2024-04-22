import pytesseract
from PIL import Image
import os
import re

# Configure tesseract to use a specific Page Segmentation Mode and OCR Engine Mode
custom_oem_psm_config = r'--oem 3 --psm 6'

def extract_text_and_rename(file_path):
    try:
        text = pytesseract.image_to_string(Image.open(file_path), config=custom_oem_psm_config)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return

    # Remove undesired characters and replace with an underscore
    text = text.replace('?', '_')

    # Use regular expression to keep only alphanumeric, underscores, and hyphens
    clean_text = re.sub(r'[^A-Za-z0-9_-]+', '_', text)

    if 'RECALL' in clean_text.upper():
        split_text = clean_text.split('RECALL')[0].strip('_')
    else:
        print(f"'RECALL' not found in {file_path}: Extracted text: {clean_text}")
        return

    new_file_name = f"{split_text}_RECALL{os.path.splitext(file_path)[1]}"

    try:
        os.rename(file_path, os.path.join(os.path.dirname(file_path), new_file_name))
        print(f"File {file_path} renamed to {new_file_name}")
    except Exception as e:
        print(f"Error renaming {file_path}: {e}")

directory = '/Users/melissaespinoza/Desktop/LLF/Social Media/Social Media Graphics/Recall-Alert-Post'
formats = {'.jpg', '.jpeg', '.png'}

for filename in os.listdir(directory):
    if os.path.splitext(filename)[1].lower() in formats:
        extract_text_and_rename(os.path.join(directory, filename))
