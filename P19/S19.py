from itertools import permutations

if __name__ == '__main__':
    s = str(input())
    k = int(s.split(" ")[1])
    s = str(s.split(" ")[0])
    permute = list(permutations(s,k))
    permute.sort()
    for i in permute:
        for j in i:
            print(j,end='')
        print("")
