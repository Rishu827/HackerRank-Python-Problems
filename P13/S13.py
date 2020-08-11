def match(s,k):
    No_match = True
    default = (-1,-1)
    result = s.find(k)
    while(result != -1):
        No_match = False
        answer = (result,result+len(k)-1)
        print(answer)
        result = s.find(k,result+1)
    if(No_match):
        print(default)

if __name__ == '__main__':
    s = str(input())
    k = str(input())
    match(s,k)
