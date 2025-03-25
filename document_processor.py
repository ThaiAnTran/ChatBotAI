# document_processor.py
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from docx import Document
import config
import os

class DocxLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        doc = Document(self.file_path)
        text = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)
        return [{"page_content": "\n".join(text), "metadata": {"source": self.file_path}}]

def process_documents():
    # Khởi tạo text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Khởi tạo embeddings
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    
    # Danh sách để lưu tất cả các chunks
    all_chunks = []
    
    # Xử lý từng tài liệu
    for doc_path in config.DOCUMENTS:
        if not os.path.exists(doc_path):
            print(f"Không tìm thấy file: {doc_path}")
            continue
            
        print(f"Đang xử lý file: {doc_path}")
        try:
            # Chọn loader dựa trên phần mở rộng file
            file_extension = os.path.splitext(doc_path)[1].lower()
            if file_extension == '.pdf':
                loader = PyPDFLoader(doc_path)
            elif file_extension == '.txt':
                loader = TextLoader(doc_path, encoding='utf-8')
            elif file_extension == '.docx':
                loader = DocxLoader(doc_path)
            else:
                print(f"Không hỗ trợ định dạng file: {file_extension}")
                continue
            
            # Load tài liệu
            pages = loader.load()
            
            # Chia nhỏ tài liệu thành các chunks
            chunks = text_splitter.split_documents(pages)
            all_chunks.extend(chunks)
            
        except Exception as e:
            print(f"Lỗi khi xử lý file {doc_path}: {str(e)}")
            continue
    
    if not all_chunks:
        print("Không có tài liệu nào được xử lý thành công!")
        return
    
    # Tạo vector store từ tất cả các chunks
    print("Đang tạo vector store...")
    vectorstore = FAISS.from_documents(all_chunks, embeddings)
    
    # Lưu vector store
    print(f"Đang lưu vector store vào {config.FAISS_INDEX_PATH}")
    vectorstore.save_local(config.FAISS_INDEX_PATH)
    print("Đã xử lý tài liệu và lưu index FAISS.")

if __name__ == "__main__":
    process_documents()