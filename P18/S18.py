from itertools import product

if __name__ == '__main__':
    a = str(input())
    a = a.split(' ')
    b = str(input())
    b = b.split(' ')
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])
    for i in product(a,b):
        print(i,end=' ')
