from PIL import Image

from pdf_to_image import Pdf2Image 
Image.MAX_IMAGE_PIXELS = 1000000000 
import time
from multiprocessing import Process, Queue



if __name__ == "__main__":
    pdf = Pdf2Image("test.pdf")
    
    #th1 = Process(target=work, args=(0, last_page//4))
    #th2 = Process(target=work, args=(last_page//4 + 1, (last_page//4)*2))
    #th3 = Process(target=work, args=((last_page//4)*2+1, (last_page//4)*3))
    #th4 = Process(target=work, args=((last_page//4)*3+1, last_page))
