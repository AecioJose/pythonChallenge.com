import re

with open('Files/fileLevel3.txt', 'r') as file:
    text = file.read()

padrao = r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'

finalWord = ''
for c in re.findall(padrao, text):
    finalWord += c[4]

print(finalWord)

# Actual -> http://www.pythonchallenge.com/pc/def/equality.html
# Next Level -> http://www.pythonchallenge.com/pc/def/linkedlist.html -> .php
