#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9

import re
import time

path='/Users/pablogarcia/Desktop/norms_temp/16164/'
file_in='step_1_translated_16164.txt'
file_out_0='step_3_subsection_0_16164.txt'
file_out_1='step_3_subsection_1_16164.txt'
file_out_2='step_3_subsection_2_16164.txt'
file_out_3='step_3_subsection_3_16164.txt'
file_out_4='step_3_subsection_4_16164.txt'

path_string_removed=path+file_in
path_section=path+file_out_0
path_subsection_1=path+ file_out_1
path_subsection_2=path+ file_out_2
path_subsection_3=path+ file_out_3
path_subsection_4=path+ file_out_4

section='\\\section{'
subsection='\\\subsection{'
hspace='\\\hspace{3mm}'
closing_curly='}'

##################
subsection_2= '\\\subsection*{'
vspace='\\\\vspace{-6mm}'

subsubsection = '\\\subsubsection*{'
hspace6='\\\hspace{6mm}'

##################################
first=r'\g<first>'
second=r'\g<second>'
#one_digit_text=r'(^\d) (.*)'   #one digit + text: Section  \section{<NUM> \hspace{3mm} <TEXT>}
remplacing_section=section+first+hspace+second+closing_curly # 1 digit + text

remplacing_sub_section=subsection+first+hspace+second+closing_curly  # d.d + text

remplacing_sub_section_2=subsection_2+first+hspace+closing_curly+'\n'+vspace  # d.d 

# \subsubsection*{first\hspace{6mm} {\normalfont  second } }

remplacing_sub_section_3=subsubsection+first+hspace6+'{\\\\normalfont'+' '+second+closing_curly+'}'  # {d.d.d+ }  + text

# remplacing_sub_section_3='\\\\textbf{'+first+'}'+' '+second  # {d.d.d+ }  + text



####################################################################################################


with open(path_string_removed,'r',encoding='utf8') as oldfile, open(path_section, 'w',encoding='utf8') as newfile: # digit + text ie. 4 hello world | 54 Hello wordl OK
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d+) (?P<second>.*)',remplacing_section, line))


####################################################################################################

with open(path_section,'r',encoding='utf8') as oldfile, open(path_subsection_1, 'w',encoding='utf8') as newfile: #Three digits + Text ok
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d+\.\d+\.\d+) (?P<second>.*)',remplacing_sub_section_3, line))

####################################################################################################



with open(path_subsection_1,'r',encoding='utf8') as oldfile, open(path_subsection_2, 'w',encoding='utf8') as newfile: #Two digits + Text ok
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d+\.\d+) (?P<second>.*)',remplacing_sub_section, line))

####################################################################################################


with open(path_subsection_2,'r',encoding='utf8') as oldfile, open(path_subsection_3, 'w',encoding='utf8') as newfile: #Two digits  OK
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d\.\d+$)',remplacing_sub_section_2, line))


####################################################################################################


with open(path_subsection_3,'r',encoding='utf8') as oldfile, open(path_subsection_4, 'w',encoding='utf8') as newfile: #four digits + Text ok
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d+\.\d+\.\d+\.\w+) (?P<second>.*)',remplacing_sub_section_3, line))

# lllllllll

# with open(path_string_removed,'r',encoding='utf8') as oldfile, open(path_section, 'w',encoding='utf8') as newfile: #One digit + Text
#     for line in oldfile:
#         newfile.write(re.sub(r'(?P<first>^\d) (?P<second>.*)',remplacing_section, line))


# # #1 r'\g<first>3\g<third>'
# #2 r'\g<first>3'


# remplacing2=first+str(i)

# new_string2=re.sub(r'(?P<first>_t7)(?P<second>\d)', remplacing2, new_string)

