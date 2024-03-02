import os
import re 
from PyPDF2 import PdfFileMerger 

#The following function merges all PDF files in a given function
#The mname argument is the name of the merged file
#The savedir arugment is the location whre the merged file will be saved
#The src argument is the directory where the PDF files are saved.By default it is set to the current directory

def alphanum_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key = alphanum_key)


def MergePDF(mname, savedir, src = os.getcwd):
    merge = PdfFileMerger()

    sorted_list = alphanum_sort(os.listdir(src))

    for item in sorted_list:
        if item.endswith("pdf"):
            merge.append(item)
            
        merge.write(savedir)
        merge.close()


print(alphanum_sort(['12 book', '4 book', '48 book', 'book']))
