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



first=r'\g<first>'
second=r'\g<second>'
third=r'\g<second>'
#one_digit_text=r'(^\d) (.*)'   #one digit + text: Section  \section{<NUM> \hspace{3mm} <TEXT>}
remplacing_section=section+first+hspace+second+closing_curly # Section + text
 
remplacing_sub_section=subsection+first+hspace+second+closing_curly  # sub section + text

remplacing_sub_section_2=subsection_2+first+hspace+closing_curly+'\n'+vspace


with open(path_string_removed,'r',encoding='utf8') as oldfile, open(path_section, 'w',encoding='utf8') as newfile: #One digit + Text
    for line in oldfile:
        newfile.write(re.sub(r'(?P<first>^\d) (?P<second>.*)',remplacing_section, line))

with open(path_section,'r',encoding='utf8') as oldfile2, open(path_subsection_1, 'w',encoding='utf8') as newfile2: #Three digits + Text
    for line in oldfile2:
        newfile2.write(re.sub(r'(?P<first>^.\.\d+\.\d+) (?P<second>.*)',remplacing_sub_section, line))

with open(path_subsection_1,'r',encoding='utf8') as oldfile3, open(path_subsection_2, 'w',encoding='utf8') as newfile3: #Two digits + Text
    for line in oldfile3:
        newfile3.write(re.sub(r'(?P<first>^.\.\d+) (?P<second>.*)',remplacing_sub_section, line))

with open(path_subsection_2,'r',encoding='utf8') as oldfile4, open(path_subsection_3, 'w',encoding='utf8') as newfile4: #Two digits 
    for line in oldfile4:
        # newfile4.write(re.sub(r'(?P<first>^\d\.\d+\.\d+$)',remplacing_sub_section_2, line))
        newfile4.write(re.sub(r'(?P<first>^\d\.\d+$)',remplacing_sub_section_2, line))

with open(path_subsection_3,'r',encoding='utf8') as oldfile5, open(path_subsection_4, 'w',encoding='utf8') as newfile5: #Three digits + Text
    for line in oldfile5:
        newfile5.write(re.sub(r'(?P<first>^.\.\d+\.\d+\.\d+) (?P<second>.*)',remplacing_sub_section, line))

# lllllllll

# with open(path_string_removed,'r',encoding='utf8') as oldfile, open(path_section, 'w',encoding='utf8') as newfile: #One digit + Text
#     for line in oldfile:
#         newfile.write(re.sub(r'(?P<first>^\d) (?P<second>.*)',remplacing_section, line))


# # #1 r'\g<first>3\g<third>'
# #2 r'\g<first>3'


# remplacing2=first+str(i)

# new_string2=re.sub(r'(?P<first>_t7)(?P<second>\d)', remplacing2, new_string)

