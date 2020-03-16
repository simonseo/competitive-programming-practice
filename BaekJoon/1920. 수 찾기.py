N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
assert len(A) == N
assert len(B) == M

A_set = set(A)

for b in B:
    print(1 if b in A_set else 0)
