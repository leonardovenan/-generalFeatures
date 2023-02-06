import random
import linecache
#read an arbritary line from a file
def get_answer():
    line_num = random.randint(1, 5)
    answer = linecache.getline("text.txt", line_num)
    return answer.strip()

result = get_answer()

print(result) 

# How to merge multiple PDFs using Python

import fitz

def merge_pdfs(pdf_list, output):
    # Create a PDF object to write the merged PDF to
    merger = fitz.open()

    # Loop through all PDFs in the list
    for pdf in pdf_list:
        # Open the PDF
        doc = fitz.open(pdf)
        # Read the PDF into the merger
        merger.insert_pdf(doc)
        # Close the PDF
        doc.close()

    # Write the merged PDF to the output file
    merger.save(output)

# Example usage
pdf_list = ['file1.pdf', 'file2.pdf', 'file3.pdf']
merge_pdfs(pdf_list, 'output.pdf')