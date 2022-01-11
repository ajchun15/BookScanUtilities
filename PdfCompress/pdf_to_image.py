import fitz
from multiprocessing import Process, Queue
#from PIL import Image
#Image.MAX_IMAGE_PIXELS = 1000000000 

def convert_pdf_to_image(file_name, thread_num):
    if thread_num >= 16:
        raise Exception('스레드 개수는 16개 이하여야 합니다.')
    
    page_num = get_last_page(file_name)
    threads = []
    
    for i in range(thread_num-1):
        thread = Process(target=convert_work, args=((page_num//thread_num)*i, (page_num//thread_num)*(i+1), file_name))
        threads.append(thread)
    thread = Process(target=convert_work, args=((page_num//thread_num)*(thread_num-1), page_num, file_name))
    threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

def convert_work(start_page, end_page, file_name):
    doc = fitz.open(file_name)
    for i in range(start_page, end_page):
        page = doc.load_page(i)
        pix = page.get_pixmap(dpi=300)
        output = "./temp/" + f'{i:06}' + ".jpeg"
        pix.pil_save(output, format="jpeg", dpi=(300, 300), quality=70)
        #pix.save(output, quality=70)

def get_last_page(file_name):
    doc = fitz.open(file_name)
    return doc.page_count