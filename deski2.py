N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# Składamy piaskownicę z jednej deski
side = arr[-1] // 4

# Składamy piaskownicę z dwóch desek
if N >= 2:
    # Dzielimy najdłuższą deskę na trzy części i bierzemy drugą najdłuższą deskę
    side = max(side, min(arr[-1] // 3, arr[-2]))
    # Dzielimy obie najdłuższe na dwie części
    side = max(side, arr[-2] // 2)

# Składamy piaskownicę z trzech desek
if N >= 3:
    # Dzielimy najdłuższą deskę na pół, żeby mieć łącznie 4 części
    side = max(side, min(arr[-1], arr[-3]))

# Składamy piaskownicę z czterech desek
if N >= 4:
    # Nic nie musimy piłować
    side = max(side, arr[-4])

print(side * side)
