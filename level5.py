from urllib.request import urlopen
import pickle

url = "http://pythonchallenge.com/pc/def/banner.p"

htmldata = urlopen(url).read()

data = pickle.loads(htmldata)

for line in data:
    line_print = ""
    for char, num in line:
        line_print += char * num
    print(line_print)
