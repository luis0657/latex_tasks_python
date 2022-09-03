#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9

bad_words = ['All rights reserved','ISO 16164:2015']

path='/Users/pablogarcia/Desktop/norms_temp/16164/'

file_input='16164_cleaned.txt'
file_output='step_0_cleaned_again_16164.txt'


path_translated=path+file_input
path_string_removed=path+file_output


with open(path_translated,'r',encoding='utf8') as oldfile, open(path_string_removed, 'w',encoding='utf8') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)