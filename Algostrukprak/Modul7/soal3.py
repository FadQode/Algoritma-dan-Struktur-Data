import re

f = open('indonesia.txt', 'r') ## membuka file.
p = r"di\s\w*"

strings = re.findall(p, f.read())
print(strings)  