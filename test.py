#!/Users/pablogarcia/opt/anaconda3/envs/test4/bin/python3.9

from googletrans import Translator

text=("How to convert some text to multiple languages")
destination_language = {
    "Spanish": "es",
    "Chinese":"zh-CN",
    "Italian":"it"
}
translator=Translator()
for key, value in destination_language.items():
    print(translator.translate(text, dest=value).text)