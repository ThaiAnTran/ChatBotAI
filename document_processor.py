# document_processor.py
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Thay đổi từ
# from langchain.document_loaders import PyPDFLoader
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores import FAISS

# Thành:
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import config

def process_document():
    # Đọc tài liệu
    loader = PyPDFLoader(config.DOCUMENT_PATH)
    documents = loader.load()
    
    # Chia nhỏ tài liệu thành các chunk
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    
    # Tạo embeddings
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    
    # Tạo và lưu index FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(config.FAISS_INDEX_PATH)
    print("Đã xử lý tài liệu và lưu index FAISS.")