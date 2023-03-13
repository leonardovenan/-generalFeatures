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
"""
# Example usage
pdf_list = ['file1.pdf', 'file2.pdf', 'file3.pdf']
merge_pdfs(pdf_list, 'output.pdf')
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name}. I am {self.age} years old'
    
    def __repr__(self):
        return f'<Person({self.name}, {self.age})>'

leo = Person('Leo', 29)

print(leo)
print(repr(leo))

# voice recorder

import sounddevice
from scipy.to.wavfile import write
fs=44200 #sample_rate
second = int(input("Entre com o tempo de duracao"))
print("Gravando...\n")
record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channems=2)
sounddevice.wait()
write("out.wav", fs, record_voice)
print("Acabando gravação. \nPor favor verifique..")
