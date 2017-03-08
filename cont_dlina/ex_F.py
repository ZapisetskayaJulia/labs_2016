def gr (N):
    for i in range(N):
        s = input().split()
        for j in range(N):
            s[j] = int(s[j])
            if s[j] != 0:
                print(i,j,s[j])

N= int(input())
graph = gr(N)