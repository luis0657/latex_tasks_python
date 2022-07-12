from itertools import count
import re
import googletrans
from googletrans import Translator

translator = Translator() 


path_source='C:/Users/gap1tl/Documents/Traduccion/Ongoing/ISO_15864_cleaned.txt'
path_translated='C:/Users/gap1tl/Documents/Traduccion/Ongoing/1_ISO_15864_translated.txt'


f_source = open(path_source, 'r',encoding='utf8')   #add encoding
f_translated = open(path_translated, 'w',encoding='utf8')   #add encoding

f_source_lines=f_source.readlines()

for line in f_source_lines:
    if not line.strip(): continue 
    result = translator.translate(line,dest='es',src='en')
    f_translated.write(result.text+'\n')

f_source.close()
f_translated.close()