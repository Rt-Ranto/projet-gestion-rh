import fitz
import os 


class AjoutParPdf:
    def __init__(self,pdf_file):
        self.__pdf_file = pdf_file

    def data_extraction(self):
        doc = fitz.open(self.__pdf_file)