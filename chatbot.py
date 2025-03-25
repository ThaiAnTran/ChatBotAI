# chatbot.py
import retriever
import ollama_interface
import config

def main():
    print("Khởi động chatbot...")
    try:
        retriever_instance = retriever.Retriever()
    except Exception as e:
        print(f"Lỗi khi tải index FAISS: {e}")
        print("Vui lòng chạy setup.py trước để xử lý tài liệu.")
        return
    
    print("Chatbot sẵn sàng! Gõ 'exit' để thoát.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        # Truy xuất các chunk liên quan
        relevant_chunks = retriever_instance.get_relevant_chunks(user_input)
        
        # Xây dựng prompt
        context = "\n".join(relevant_chunks)
        prompt = f"Context:\n{context}\n\nQuestion: {user_input}\n\nAnswer:"
        
        # Gửi đến Ollama và nhận câu trả lời
        response = ollama_interface.get_response(prompt)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()