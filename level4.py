from urllib.request import urlopen
from re import findall

urlDefault = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = urlDefault + "12345"
numbersFounds = []
pdr = r"\d+"


for n in range(400):
    print(url)
    html = urlopen(url=url)
    text = html.read().decode("utf8")
    numbers = findall(pdr, text)
    numbersFounds.append(numbers)
    if len(numbers) == 0:
        print("\033[32mVERIFIQUE A URL:\033[m \n>>>", url)
        break
    if len(numbers) > 1:
        number = numbers[1]
    else:
        number = numbers[0]
    url = urlDefault + number
print("\nNumeros Encontrados: \n", numbersFounds)
