import fitz
from multiprocessing import Process, Queue

def convert_pdf_to_image_multiThread(file_name, thread_num):
    page_num = get_last_page(file_name)
    th1 = Process(target=convert_pdf_to_image, args=(0, page_num, file_name))
    th1.start()
    th1.join()

def convert_pdf_to_image(start_page, end_page, file_name):
    doc = fitz.open(file_name)
    for i in range(start_page, end_page):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        output = "./hope/" + str(i) + ".tiff"
        pix.save(output)

def get_last_page(file_name):
    doc = fitz.open(file_name)
    return doc.page_count