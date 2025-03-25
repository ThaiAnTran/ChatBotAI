# Chatbot Giáo Luật Công Giáo

Chatbot được thiết kế để trả lời các câu hỏi về Giáo Luật Công Giáo, sử dụng công nghệ AI và xử lý ngôn ngữ tự nhiên.

## Tính năng

- Trả lời câu hỏi về nội dung Giáo Luật
- Giải thích các điều khoản và quy định
- Cung cấp thông tin về cấu trúc và tổ chức của Giáo Luật
- Hỗ trợ tìm kiếm thông tin cụ thể
- Hỗ trợ đọc nhiều định dạng file (PDF, TXT, DOCX)
- API RESTful để tích hợp với các ứng dụng khác

## Cấu trúc dự án

```
Demo-chat-ollama/
├── data/                   # Thư mục chứa tài liệu
│   ├── Giao-Luat-1983.pdf  # File PDF chính
│   ├── gioi-thieu.txt      # File text giới thiệu
│   └── faiss_index/        # Thư mục chứa index FAISS
├── venv/                   # Môi trường ảo Python
├── api.py                  # API server FastAPI
├── chatbot.py             # Lớp chính của chatbot
├── config.py              # Cấu hình hệ thống
├── document_processor.py  # Xử lý tài liệu
├── ollama_interface.py    # Giao tiếp với Ollama
├── retriever.py           # Truy xuất thông tin
├── setup.py               # Script khởi tạo
└── requirements.txt       # Các thư viện cần thiết
```

## Yêu cầu hệ thống

### Yêu cầu tối thiểu (cho model nhẹ)

- Python 3.8 trở lên
- Ollama (phiên bản 0.6.2 trở lên)
- 4GB RAM trở lên
- 5GB dung lượng ổ đĩa trống
- CPU: Intel Core i3 hoặc tương đương

### Yêu cầu khuyến nghị (cho model lớn)

- Python 3.8 trở lên
- Ollama (phiên bản 0.6.2 trở lên)
- 8GB RAM trở lên
- 10GB dung lượng ổ đĩa trống
- CPU: Intel Core i5 hoặc cao hơn
- GPU: NVIDIA với 4GB VRAM (tùy chọn, để tăng tốc)

### Các model Ollama được hỗ trợ

1. Model nhẹ (cho máy yếu):

   - `mistral`: ~4GB, tốc độ nhanh, độ chính xác khá
   - `neural-chat`: ~4GB, tốc độ nhanh, phù hợp cho chat
   - `phi`: ~2.7GB, rất nhẹ, tốc độ cao

2. Model trung bình:

   - `llama2`: ~4GB, cân bằng giữa tốc độ và chất lượng
   - `codellama`: ~4GB, tốt cho code và text

3. Model lớn (cho máy mạnh):
   - `llama3.1`: ~8GB, chất lượng cao, tốc độ chậm hơn
   - `mixtral`: ~13GB, chất lượng rất cao, yêu cầu nhiều tài nguyên

Để sử dụng model nhẹ, cập nhật `OLLAMA_MODEL` trong `config.py`:

```python
OLLAMA_MODEL = "mistral"  # hoặc "neural-chat" hoặc "phi"
```

## Cài đặt

1. Cài đặt Ollama:

   - Truy cập https://ollama.ai/download
   - Tải và cài đặt Ollama cho Windows
   - Chạy lệnh sau để tải model:

     ```bash
     # Cho model nhẹ
     ollama pull mistral

     # Hoặc cho model trung bình
     ollama pull llama2

     # Hoặc cho model lớn
     ollama pull llama3.1
     ```

2. Cài đặt môi trường Python:

   ```bash
   # Tạo môi trường ảo
   python -m venv venv

   # Kích hoạt môi trường ảo
   .\venv\Scripts\activate

   # Cài đặt các thư viện
   pip install -r requirements.txt
   ```

3. Chuẩn bị dữ liệu:
   - Đặt các file tài liệu vào thư mục `data/`
   - Cập nhật danh sách file trong `config.py`
   - Chạy script khởi tạo:
     ```bash
     python setup.py
     ```

## Cách sử dụng

### 1. Chạy API Server

```bash
python api.py
```

Server sẽ chạy tại http://localhost:8000

### 2. Sử dụng API

#### Gửi câu hỏi

```bash
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"text": "giáo luật nói về gì"}'
```

#### Xem tài liệu API

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 3. Thêm tài liệu mới

1. Đặt file mới vào thư mục `data/`
2. Thêm đường dẫn file vào danh sách `DOCUMENTS` trong `config.py`
3. Chạy lại setup:
   ```bash
   python setup.py
   ```

## Hỗ trợ định dạng file

- PDF (.pdf)
- Text (.txt)
- Microsoft Word (.docx)

## Cấu hình

Các thông số cấu hình trong `config.py`:

- `DOCUMENTS`: Danh sách file tài liệu
- `FAISS_INDEX_PATH`: Đường dẫn lưu index FAISS
- `OLLAMA_MODEL`: Model Ollama sử dụng
- `EMBEDDING_MODEL`: Model embedding sử dụng
- `OLLAMA_API_URL`: URL API của Ollama
- `SYSTEM_PROMPT`: Prompt hệ thống cho chatbot

## Xử lý lỗi thường gặp

1. Lỗi "404 Not Found" khi gọi Ollama API:

   - Kiểm tra Ollama đã được cài đặt và đang chạy
   - Kiểm tra model đã được tải về

2. Lỗi khi xử lý file:

   - Kiểm tra file tồn tại trong thư mục data/
   - Kiểm tra định dạng file được hỗ trợ
   - Kiểm tra quyền truy cập file

3. Lỗi khi khởi tạo vector store:

   - Xóa thư mục faiss_index và chạy lại setup.py
   - Kiểm tra dung lượng ổ đĩa

4. Lỗi thiếu bộ nhớ:
   - Thử sử dụng model nhẹ hơn
   - Giảm kích thước chunk trong document_processor.py
   - Đóng các ứng dụng khác để giải phóng bộ nhớ

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork dự án
2. Tạo branch mới
3. Commit các thay đổi
4. Push lên branch
5. Tạo Pull Request
