from langchain_community.document_loaders import TextLoader, CSVLoader
from langchain_community.document_loaders.pdf import PyPDFLoader


class Loader:
    def __init__(self, file_path, encoding):
        self.file_path = file_path
        self.encoding = encoding

    def get_txt_loader(self):
        loader = TextLoader(file_path=self.file_path, encoding=self.encoding)
        return loader

    def get_pdf_loader(self):
        loader = PyPDFLoader(file_path=self.file_path, extract_images=True)
        return loader

    def get_csv_loader(self):
        loader = CSVLoader(file_path=self.file_path, encoding=self.encoding)
        return loader
