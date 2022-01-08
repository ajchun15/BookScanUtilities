import fitz

class Pdf2Image:
    def __init__(self, file_name):
        self.doc = fitz.open(file_name)
    
    def convert_pdf_to_image(self, start_page, end_page):
        for i in range(start_page, end_page):
            page = self.doc.load_page(i)
            pix = page.get_pixmap()
            output = "./hope/" + str(i) + ".tiff"
            pix.save(output)
            
    def get_last_page(self):
        return self.doc.page_count
'''

def convert_pdf_to_image(start_page, end_page, filename):
    doc = fitz.open(filename)
    
    for i in range(start_page, end_page+1):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        output = "./hope/" + str(i) + ".tiff"
        pix.save(output)
        
#doc.page_count

'''