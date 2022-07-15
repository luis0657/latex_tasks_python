#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9


from itertools import count
import re
from googletrans import Translator
# To install google trans:pip install googletrans==3.1.0a0 
translator = Translator() 


path='/Users/pablogarcia/Desktop/norms_temp/'

file_input='step_0_cleaned_14222.txt'
file_output='step_1_translated_14222.txt'

path_source=path+file_input
path_translated=path+file_output


f_source = open(path_source, 'r',encoding='utf8')   #add encoding
f_translated = open(path_translated, 'w',encoding='utf8')   #add encoding

f_source_lines=f_source.readlines()

for line in f_source_lines:
    if not line.strip(): continue 
    result = translator.translate(line,dest='es',src='en')
    f_translated.write(result.text+'\n')

f_source.close()
f_translated.close()