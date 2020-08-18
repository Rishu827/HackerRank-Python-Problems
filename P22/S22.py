import re

def ValidCardNumber(num): 
    if(re.match(r'^[456]{1}',num)==None):
        return "Invalid"
    
    if(re.match(r'(?=^[0-9]{16}$)|(?=^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$)',num)==None):
        return "Invalid"
    
    num = num.replace("-",'')
    a = re.findall(r'([0-9])\1\1\1',num) 
    if(len(a) != 0):
        return "Invalid"

    return "Valid"

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        card_num = input()
        print(ValidCardNumber(card_num))
