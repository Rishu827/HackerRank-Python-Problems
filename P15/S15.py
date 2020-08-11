import re

def ValidMobile(s):
    if(len(s)>10):
        return "NO"
    regex_pattern = r"\b[789][0-9]{9}"
    answer = re.match(regex_pattern,s)
    if(answer):
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        s = str(input())
        print(ValidMobile(s))
