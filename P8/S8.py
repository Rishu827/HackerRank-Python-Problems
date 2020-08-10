# Enter your code here. Read input from STDIN. Print output to STDOUT
def Cap_Room(k,l):
    l.sort()
    length = len(l)

    group = length//k #number of group

    for i in range(0,group):
        curr = i*k
        nxt = curr+k-1
        if(l[curr] != l[nxt-1]):
            if(l[curr] == l[curr+1]):
                return(l[nxt])
            else:
                return(l[curr])
    return(l[-1])


if __name__ =='__main__':
    k = int(input()) #size of group
    l1 = str(input())
    l = l1.split(" ")
    print(Cap_Room(k,l))
    
    
