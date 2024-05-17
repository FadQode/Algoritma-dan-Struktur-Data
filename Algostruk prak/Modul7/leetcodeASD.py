def numUniqueEmails(emails):
    sent = []
    for i in emails:
        splitted = i.split("@")
        if "." in splitted[0]:
            splitted[0] = splitted[0].replace(".", "") 
        if "+" in splitted[0]:
            for j in range(len(splitted[0])):
                if splitted[0][j] == "+":
                    splitted[0] = splitted[0].replace(splitted[0][j:], "")
                    break
        trumail = splitted[0] + "@" + splitted[1] 
        if trumail not in sent:
            sent.append(trumail)    
    return sent  

ls = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
ls2 = ["test.emailalex@leetcode.com","test.e.mailbob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(ls2))