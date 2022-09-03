#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9

from hashlib import new
import re

#This code creates a good indexing for https://text2bib.economics.utoronto.ca/index.php/index

def new_index(string1,i):
    result1= re.sub(r"(^@\w+{)(\w+,)",r"\1b"+"{}_ISO14222,".format(i),string1)
    return result1

path='/Users/pablogarcia/Desktop/norms_temp/'
file_in='14222_bib.txt'
file_out='14222_bib_indexed.txt'

path_source=path+file_in
path_output=path+file_out


f = open(path_source, "r")
copy = open(path_output, "w")
new_line=""
i=1
for line in f:
    new_line=new_index(line,i)
    copy.write(new_line)
    if new_line != line:
        i=i+1
f.close()
copy.close()