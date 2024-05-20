def numUniqueEmails(emails):
    sent = []
    for i in emails:
        name, domain = i.split("@")
        trumail = name.split("+")[0].replace(".","") +  "@" + domain
        if trumail not in sent:
            sent.append(trumail)    
    return sent  

ls = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
ls2 = ["test.emailalex@leetcode.com","test.e.mailbob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(ls2))