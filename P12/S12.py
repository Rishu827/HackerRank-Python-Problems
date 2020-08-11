import re

def VowelMatch(s):
    No_match = True
    for i in re.finditer("[aeiouAEIOU][aeiouAEIOU]+",s):
        start = i.span()[0]
        end = i.span()[1]
        if((start != 0 ) and (end != len(s))):
            bool_start = re.match("[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]",s[start-1])
            bool_end = re.match("[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]",s[end])
            if((bool_start != None) and (bool_end != None)):
                No_match = False
                print(i.group())

    if(No_match):
        print(-1)

if __name__== '__main__':
    s = str(input())
    VowelMatch(s)
