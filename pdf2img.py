# -*- coding: utf-8 -*-

"""
pip install pymupdf
"""
import os
import fitz

pdf_dir=[]

pdfPath = './pdf'
imagePath = './image'

def get_file():
    docunames = os.listdir(pdfPath)
    for docuname in docunames:
        if os.path.splitext(docuname)[1] == '.pdf':# all pdf file in pdf folder 
            pdf_dir.append(docuname)
            
def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(pdfPath+'/'+pdf)
        pdf_name = os.path.splitext(pdf)[0]
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            # scale factor of each side 
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)

            pm.writePNG(imagePath+'/'+pdf_name+'_%s.png' % pg)
            
if __name__ == '__main__':
    get_file()
    if not os.path.exists(imagePath):# is image folder exist
        os.makedirs(imagePath) # create folder if not exist
    conver_img()