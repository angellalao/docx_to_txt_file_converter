#!/usr/bin/env python3

from convert_docx_to_txt import batch_convert
import os

if __name__ == "__main__":
    input_folder_path = os.getcwd()
    batch_convert(input_folder_path)