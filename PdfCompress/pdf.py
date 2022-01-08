import tkinter
import pdf2image
import tempfile
import tkinter
from pdf2image.pdf2image import convert_from_path
from PIL import Image 
Image.MAX_IMAGE_PIXELS = 1000000000 
import time

start = time.time()

image_from_path = convert_from_path('Programming Language 1.pdf', output_folder="te", poppler_path="poppler-21.11.0/Library/bin", fmt="tiff", thread_count=4)

end = time.time()

print("이미지 변환 1차: " + str(end-start))

start = time.time()

for i, page in enumerate(image_from_path):
    page.save("./hope/" + str(i) +".jpeg", "jpeg")

end = time.time()
print("이미지 변환 1차: " + str(end-start))

'''

import fitz

pdffile = 'test.pdf'
doc = fitz.open(pdffile)
print(doc.page_count)
#page = doc.loadPage(3)
#pix = page.get_pixmap()
#output = "out.png"
#pix.save(output)
'''