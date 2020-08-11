import re

def sub(s):
    while(" && " in s): 
        s=re.sub(" && "," and ",s)
    while("  \|\| " in s):
        s=re.sub(" \|\| "," or ",s)
    print(s)

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        s = str(input())
        sub(s)
