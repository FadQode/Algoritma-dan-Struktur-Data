import re
nim = "l200220234"
f = open('kei.html', 'r', encoding='latin-1') ## membuka file.
p2 = r"/wiki/\w*"
country = re.findall(p2, f.read())
f.close

g = open('kei.html', 'r', encoding='latin-1')
kei =  re.findall(r"</a></td>\s<td>(\d+\.\d{2}|\d+)" , g.read() )

country = country[country.index("/wiki/Denmark"):country.index("/wiki/Zambia") + 1]
index = []
for i in range(len(kei)):
    country[i] = country[i].replace("/wiki/", "")
    ind = (country[i], kei[i])
    index.append(ind)
print(index)    
print(nim)

