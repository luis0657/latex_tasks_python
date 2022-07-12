bad_words = ['Todos los derechos reservados', 'ISO 15864:2021(E)']

path_translated='C:/Users/gap1tl/Documents/Traduccion/Ongoing/1_ISO_15864_translated.txt'
path_string_removed='C:/Users/gap1tl/Documents/Traduccion/Ongoing/2_ISO_15864_string_removed.txt'


with open(path_translated,'r',encoding='utf8') as oldfile, open(path_string_removed, 'w',encoding='utf8') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)