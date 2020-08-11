import re
import email.utils

def Validation_Email(mail):
    regex_pattern = r"\b[A-Za-z][\d\w._-]+[@][a-zA-Z]+\.[a-zA-Z]{1,3}"
    length = len(mail)
    match = re.match(regex_pattern,mail)
    if(match==None):
        return False
    if(match.span()[1] != length):
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        email_id = str(input())
        mail = email.utils.parseaddr(email_id)
        answer = Validation_Email(mail[1])
        if(answer):
            print(email.utils.formataddr(mail))

