def Occurence(s):
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            if((ord(s[i])-97<26 and ord(s[i])-97>-1) or (ord(s[i])-65<26 and ord(s[i])-65>-1) or (ord(s[i])-48<10 and ord(s[i])-48>-1)):
                return s[i]
    return -1

if __name__ == '__main__':
    s = str(input())
    print(Occurence(s))
