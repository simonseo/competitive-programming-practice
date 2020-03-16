import sys

N = int(input())
P = [0] + [int(x) for x in input().split()]
d = [0]*(N+1)

for n in range(1,N+1): #n=1~N
    for i in range(n): #i=0~n-1
        if d[i] + P[n-i] > d[n]:
            d[n] = d[i] + P[n-i]

print(d[N])