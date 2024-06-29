import re

f = open('kei.html', 'r', encoding='utf-8-sig')  ## membuka file
 # Matches <td> with 3-digit float

kei =   re.findall(r"\d+\.\d{2}", f.read() )

print(kei)