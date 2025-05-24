import os

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from openai import OpenAI

def get_vector_db():
    # 加载数据
    loader = TextLoader('C:/Users/mingxi/Desktop/projects/llmd/resource/rag_test.txt', 'utf-8')
    documents = loader.load()

    # 分割文本
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=200, chunk_overlap=20)
    texts = text_splitter.split_documents(documents)

    # debug使用
    # for i, text in enumerate(texts):
    #     print("chunk" + str(i) + ": " + str(text))
    # print("-" * 40)

    # 初始化嵌入模型
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # 创建向量存储
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore


def retrieve_docs(query, vectorDB):
    docs = vectorDB.similarity_search(query)
    return docs


def main():
    while True:
        query = input("请输入你的问题（输入 '退出' 结束对话）：")
        if query == '退出':
            break

        vectorstore = get_vector_db()
        docs = retrieve_docs(query, vectorstore)
        answer = generate_response(query, docs)
        print(answer)


if __name__ == "__main__":
    main()