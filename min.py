N = list(map(int, input().split()))
N.sort()
print(N)
if N[0] == N[1] == 0:
    (N[0], N[2]) = (N[2], N[0])
elif N[0] == 0:
    (N[0], N[1]) = (N[1], N[0])
print(N[0], N[1], N[2], sep='')
