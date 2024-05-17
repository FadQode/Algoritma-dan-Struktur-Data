import re

s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.search(r'([\w.-]+)@([\w.-]+)', s) ## perhatikan posisi () di polanya
if cocok:
    print(f"{cocok.group()}") ## ’dita-b@google.com’ (keseluruhan teks yang cocok)
    print(f"{cocok.group(1)}")  ## ’google.com’ (host-nya, yakni group 1)
    print(f"{cocok.group(2)}")  ## ’dita-b’ (username-nya, yakni group 1)