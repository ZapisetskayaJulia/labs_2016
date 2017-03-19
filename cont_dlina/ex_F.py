#Матрица смежности в список ребер

def read_graph ():
    N = int(input())
    for i in range(N):
        s = input().split()
        for j in range(N):
            if int(s[j]) != 0:
                print(i,j,int(s[j]))


graph = read_graph()