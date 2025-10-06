import os
import csv
import datetime
from pathlib import Path
from collections import Counter


data_dir = "./doc"
output_csv = "metadata.csv"

STOPWORDS = {
    "là", "của", "và", "trong", "với", "cho", "một", "được", 
    "đến", "này", "các", "đó", "khi", "như", "từ", "thì", 
    "ra", "ở", "nên", "có", "hay", "nếu", "vì"
}

# Hàm đếm số từ
def count_words(text):
    return len(text.split())

#Hàm tạo ra từ khóa
def generate_tags(text, top_n=3):
    words = [w.lower() for w in text.split() if w.isalpha() and w.lower() not in STOPWORDS]
    return ", ".join([w for w, _ in Counter(words).most_common(top_n)])

def extract_topic_from_title(first_line: str) -> str:
        # Ví dụ: "===== Computer Vision - phần mở rộng 1 ====="
    line = first_line.strip("= ").strip()
    if "- phần mở rộng" in line:
        return line.split("- phần mở rộng")[0].strip()
    return line




rows = []
for i, filename in enumerate(os.listdir(data_dir), start=1):
    filepath = os.path.join(data_dir, filename)
    if filename.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        content = "".join(lines)
            
        #Lấy topic từ dòng đầu tiên
        topic = extract_topic_from_title(lines[0]) if lines else "Không rõ"
        
        num_words = count_words(content)
        auto_tags = generate_tags(content)
        
        row = {
            "ID": i,
            "Tên file": filename,
            "Chủ đề": topic,
            "Đường dẫn": str(data_dir),
            "Số từ": num_words,
            "Ngày tạo": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Từ khóa": f"{topic}, {auto_tags}"
        }
        
        rows.append(row)
        
with open(output_csv, "w", newline="", encoding="utf-8-sig") as csvfile:
    fieldnames  = ["ID","Tên file","Chủ đề","Đường dẫn", "Số từ", "Ngày tạo", "Từ khóa"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames )
    writer.writeheader()
    writer.writerows(rows)
    
print(f"Da duyet {len(rows)} file va tao metadata CSV: {output_csv}")
