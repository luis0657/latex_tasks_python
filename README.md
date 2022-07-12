# latex_tasks_python
Scripts to add basic latex syntax.

python script to delete certain phrases from the document



Pre-Process: 
a) Copy text to a .txt file
b) Clean data: it means delete tables, images, and change shall to "must", should to "it is recommended". 

Process with python scripts:

1. Translate the file with the 1_regex_translate_file.py
2. Delete lines with specific phrases or words (for example repetitive trademarks)
3. Add the sections and subsections according to the patterns, \d, \d.\d, \d.\d.\d. etc.