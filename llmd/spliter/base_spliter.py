from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Spliter:
    def __init__(self, chunk_size=None, chunk_overlap=None, separators=None):
        self.chunk_size = chunk_size or 200
        self.chunk_overlap = chunk_overlap or 20
        self.separators= separators or ["\n\n", "\n", " ", ""]

    def get_character_spliter(self):
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter

    def get_recursive_character_spliter(self):
        text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return text_splitter

