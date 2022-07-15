#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9

bad_words = ['Todos los derechos reservados', 'ISO 15864:2021(E)','ISO 14222:2022(E)']

path='/Users/pablogarcia/Desktop/norms_temp/'

file_input='step_1_translated_14222.txt'
file_output='step_2_cleaned_again_14222.txt'


path_translated=path+file_input
path_string_removed=path+file_output


with open(path_translated,'r',encoding='utf8') as oldfile, open(path_string_removed, 'w',encoding='utf8') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)