import string

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq   ypc " \
          "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
          "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
          "ynnjw ml rfc spj."

message2 = "map"

table = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])

print(message.translate(table)) # i hope you didnt translate it by hand. thats what computers   are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
print(message2.translate(table))# ocr

# Actual -> http://www.pythonchallenge.com/pc/def/map.html
# Next Level -> http://www.pythonchallenge.com/pc/def/ocr.html