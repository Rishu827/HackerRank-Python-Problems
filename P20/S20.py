from itertools import product

if __name__ == '__main__':
    in1 = input()
    k,m = (in1.split(' '))
    k,m=int(k),int(m)

    cases = [None]*k
    for i in range(k):
        temp = str(input())
        cases[i] = temp.split(' ')
        cases[i] = list(set(cases[i]))
        for j in range(len(cases[i])):
            cases[i][j] = int(cases[i][j])%m

    possible_ans = list(product(*cases))

    solution = 0
    for i in possible_ans:
        temp_sol = 0
        for j in i:
            temp_sol = (temp_sol + int(j)**2)%m
        if(temp_sol>solution):
            solution=temp_sol
            print(i,solution)

    print(solution)
    
