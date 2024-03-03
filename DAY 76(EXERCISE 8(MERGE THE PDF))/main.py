import PyPDF2
from PyPDF2 import PdfMerger, PdfReader
mergeFile = PyPDF2.PdfMerger()
mergeFile.append(PyPDF2.PdfReader('Cracking-the-Coding-Interview-6th-Edition-189-Programming-Questions-and-Solutions.pdf', 'r'))
mergeFile.append(PyPDF2.PdfReader('Introduction_to_algorithms-3rd Edition.pdf', 'r'))
mergeFile.write("CODING BOOKS.pdf")
