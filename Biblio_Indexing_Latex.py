from hashlib import new
import re

#This code creates a good indexing for https://text2bib.economics.utoronto.ca/index.php/index

def new_index(string1,i):
    result1= re.sub(r"(^@\w+{)(\w+,)",r"\1b"+"{},".format(i),string1)
    return result1


f = open("/Users/pablogarcia/Google Drive/Drive/UPIITA/Servicio Social/Traduccion/ISO_14222-2022/40289-221007-BIB.txt", "r")
copy = open("/Users/pablogarcia/Google Drive/Drive/UPIITA/Servicio Social/Traduccion/ISO_14222-2022/221007-BIB.txt", "w")
new_line=""
i=1
for line in f:
    new_line=new_index(line,i)
    copy.write(new_line)
    if new_line != line:
        i=i+1
f.close()
copy.close()