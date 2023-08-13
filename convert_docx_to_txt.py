#!/usr/bin/env python3

from docx import Document
import os

def convert_docx_to_txt(input_path):
    if not input_path.endswith(".docx"):
        print(f"{input_path} is not a .docx file")
        return
    
    document = Document(input_path)
    text = ""
    output_path = os.path.splitext(input_path)[0] + ".txt"

    for paragraph in document.paragraphs:
        text = text + paragraph.text + "\n"

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

def batch_convert(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            input_path = os.path.join(folder_path, filename)
            convert_docx_to_txt(input_path)
            print(f"Converted: {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 convert_docx_to_txt.py <input_file.docx>")
    else:
        input_path = sys.argv[1]
        convert_docx_to_txt(input_path)
