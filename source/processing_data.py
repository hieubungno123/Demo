import os
import re
from pathlib import Path


data_dir = "./doc"
processed_dir = "./data_processed"

# Tao thu muc neu khong co
os.makedirs(processed_dir, exist_ok=True)

STOPWORDS = {
    "là", "của", "và", "trong", "với", "cho", "một", "được", 
    "đến", "này", "các", "đó", "khi", "như", "từ", "thì", 
    "ra", "ở", "nên", "có", "hay", "nếu", "vì"
}


def preprocess_text(text):
    #B2 lowercase
    text = text.lower()
    
    # B3: loại bỏ ký tự đặc biệt, số, dấu câu (chỉ giữ chữ cái và khoảng trắng)
    text = re.sub(r"[^a-zA-ZÀ-ỹ\s]", " ", text)
    
    #B4: Tach tu
    tokens = text.split()
    
    #B5: loại bỏ stopwords
    tokens = [word for word in tokens if word not in STOPWORDS]
    
    # Ghép lại thành văn bản sạch
    return " ".join(tokens)
    
# B1: duyệt qua tất cả file trong ./doc
for filename in os.listdir(data_dir):
    filepath = os.path.join(data_dir, filename)
    if filename.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        processed_text = preprocess_text(content)
        
    # Lưu vào ./Data_Processed với cùng tên file
        outpath = os.path.join(processed_dir, filename)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(processed_text)
            
        
print(" Hoan tat xu ly")
