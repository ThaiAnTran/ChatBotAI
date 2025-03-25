# config.py
# Danh sách các tài liệu cần xử lý
DOCUMENTS = [
    "data/Giao-Luat-1983.pdf",
    "data/gioi-thieu.txt",
    "data/giao-luat.docx",  # Thêm file DOCX
    # Thêm các file khác vào đây
]

FAISS_INDEX_PATH = "data/faiss_index"
OLLAMA_MODEL = "llama3.1"  # Changed from llama2 to llama3.1
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# System prompt cho chatbot
SYSTEM_PROMPT = """Tôi là một chatbot được thiết kế để trả lời các câu hỏi về [Tên tài liệu]. 
Tôi có thể:
1. Trả lời các câu hỏi về nội dung của Giáo Luật
2. Giải thích các điều khoản và quy định
3. Cung cấp thông tin về cấu trúc và tổ chức của Giáo Luật
4. Hỗ trợ tìm kiếm thông tin cụ thể trong Giáo Luật

Tôi được huấn luyện trên cơ sở dữ liệu của Nomads cung cấp với các tài liệu liên quan. 
Tôi sẽ cố gắng trả lời chính xác và hữu ích nhất có thể."""