N = int(input())
programs = [int(x) for x in input().split()]

M = int(input())
disks = [int(x) for x in input().split()]

programs.sort()
disks.sort()

result = 0
i = 0
j = 0

while i < N and j < M:
    if programs[i] > disks[j]:
        j += 1
    else:
        result += 1
        i += 1
        j += 1

print(result)
