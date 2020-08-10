# Enter your code here. Read input from STDIN. Print output to STDOUT
def Superset(a,list_set,n):
    for i in range(0,n):
        for j in list_set[i]:
            if (j not in a):
                return False

        if(len(list_set[i])==len(a)):
            return False
    
    return True


if __name__ == '__main__':
    a = input()
    a = a.split(' ')

    n = int(input())
    list_set = [None]*n
    for i in range(0,n):
        b = input()
        b = b.split(' ')
        list_set[i] = b
    
    print(Superset(a,list_set,n))
