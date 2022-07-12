import re
import time


path_string_removed='C:/Users/gap1tl/Documents/Traduccion/Ongoing/2_ISO_15864_string_removed.txt'
path_section='C:/Users/gap1tl/Documents/Traduccion/Ongoing/3_ISO_15864_section.txt'
path_subsection_1='C:/Users/gap1tl/Documents/Traduccion/Ongoing/4_ISO_15864_subsection_1.txt'
path_subsection_2='C:/Users/gap1tl/Documents/Traduccion/Ongoing/5_ISO_15864_subsection_2.txt'
path_subsection_3='C:/Users/gap1tl/Documents/Traduccion/Ongoing/6_ISO_15864_subsection_3.txt'


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
        newfile2.write(re.sub(r'(?P<first>^\d\.\d+\.\d) (?P<second>.*)',remplacing_sub_section, line))

with open(path_subsection_1,'r',encoding='utf8') as oldfile3, open(path_subsection_2, 'w',encoding='utf8') as newfile3: #Two digits + Text
    for line in oldfile3:
        newfile3.write(re.sub(r'(?P<first>^\d\.\d+) (?P<second>.*)',remplacing_sub_section, line))

with open(path_subsection_2,'r',encoding='utf8') as oldfile4, open(path_subsection_3, 'w',encoding='utf8') as newfile4: #Two digits + Text
    for line in oldfile4:
        newfile4.write(re.sub(r'(?P<first>^\d\.\d+\.\d+$)',remplacing_sub_section_2, line))

# #1 r'\g<first>3\g<third>'
# #2 r'\g<first>3'


# remplacing2=first+str(i)

# new_string2=re.sub(r'(?P<first>_t7)(?P<second>\d)', remplacing2, new_string)

