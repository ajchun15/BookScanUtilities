from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000 
import time
import pdf_to_image



if __name__ == "__main__":
    pdf_to_image.convert_pdf_to_image_multiThread(0, 10, "test.pdf", 1)
    
