# Enter your code here. Read input from STDIN. Print output to STDOUT
def Subset(a,b):
    a.sort()
    b.sort()
    for i in a:
          if(i not in b):
                return False
    return True


if __name__ == '__main__':
    test_case = int(input())

    for i in range(0,test_case):
        len_a = int(input())
        a = input()
        a = a.split(' ')

        len_b = int(input())
        b = input()
        b = b.split(' ')

        if(len_a>len_b):
            print(False)    
        else:
            print(Subset(a,b))
        
