# retriever.py
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import config

class Retriever:
    def __init__(self):
        embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
        self.vectorstore = FAISS.load_local(config.FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    
    def get_relevant_chunks(self, query, k=3):
        # Truy xuất top-k chunk liên quan
        docs = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]