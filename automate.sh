#!/bin/bash

while true; do
    changed_file=$(fswatch -1 .) # Replace with path to folder
    echo "Change detected: $changed_file"
    if [[ $changed_file == *.docx ]]; then
        echo "Converting: $changed_file"
        python3 ./convert_docx_to_txt.py "$changed_file" # Replace with path to python script
        echo "Conversion complete"
    fi
done