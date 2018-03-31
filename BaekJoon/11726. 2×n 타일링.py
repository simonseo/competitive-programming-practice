def fib(N):
    a1, a2 = 0, 1
    for i in range(1,N+1): #1~N
        a3 = a1 + a2
        a1, a2 = a2, a3
    return a3

print(fib(int(input()))%10007)