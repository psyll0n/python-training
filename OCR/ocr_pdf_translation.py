#! python3

# Explanation: This code allows you to convert a scanned PDF into a text format by 
# using Optical Character Recognition. 
#
# Libraries:
#
# * fitz (PyMuPDF): Used for loading and working with the PDF document.
# * pytesseract: An OCR tool that reads text from images.
# * pdf2image: Converts PDF pages into images which can be processed by pytesseract.
# 
# Process:
#
# * The PDF is first converted into images using convert_from_path.
# * Each image is then processed using pytesseract to extract the text.
# 
# Output: The text extracted from OCR is printed and can also be saved to a file.

import fitz  # PyMuPDF for reading the PDF
import pytesseract  # OCR library
from pdf2image import convert_from_path  # Convert PDF pages to images

# Load the PDF file
pdf_file = '/mnt/data/example_document.pdf'
doc = fitz.open(pdf_file)

# Convert PDF to images
images = convert_from_path(pdf_file)

# Perform OCR on each image
ocr_text = ""
for image in images:
    ocr_text += pytesseract.image_to_string(image)

# Displaying the first 2000 characters to verify OCR output
print(ocr_text[:2000])

# If you want to save the OCR text to a file
with open("/mnt/data/translated_text.txt", "w", encoding="utf-8") as file:
    file.write(ocr_text)

