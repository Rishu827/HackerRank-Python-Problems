# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ =='__main__':
    k = int(input()) #size of group
    l1 = str(input("enter the list"))
    print(l1)
    l = l1.split(" ")

    while ' ' in l:
        l = l.remove(' ')
    l = l.sort()
    print(l)
    length = len(l)

    group = length//k #number of group

    for i in range(0,group):
        curr = i*group
        nxt = curr+group
        if(l[curr] != l[nxt-1]):
            if(l[curr] == l[curr+1]):
                print(l[nxt])
            else:
                print(l[curr])
