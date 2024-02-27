from PyPDF2 import PdfReader, PdfWriter
from copy import deepcopy


class PDFEditor:
    def __init__(self, source_path):
        self.file_name = source_path.split("/")[-1].split(".")[0]
        self.source_path = source_path
        self.pdf_reader = PdfReader(self.source_path)
        self.pdf_writer = PdfWriter()

    def save_pdf(self, new_file_name=None):
        """
        Save the new pdf file

        :param new_file_name: str
        """
        if new_file_name:
            self.file_name = new_file_name
        if self.file_name.split(".")[-1] == "pdf":
            self.pdf_writer.write(f"{self.file_name}")
        else:
            self.pdf_writer.write(f"{self.file_name}.pdf")

    def divide_double_pages(self):
        """
        Divide the double pages into two single pages
        """
        for file_page in self.pdf_reader.pages:
            page = deepcopy(file_page)
            page.mediabox.bottom = 0
            page.mediabox.top = page.mediabox.top / 2
            self.pdf_writer.add_page(page)
            page = deepcopy(file_page)
            page.mediabox.bottom = page.mediabox.top / 2
            page.mediabox.top = page.mediabox.top
            self.pdf_writer.add_page(page)

