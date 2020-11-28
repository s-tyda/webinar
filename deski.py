
# Pierwsza metoda - z sortowaniem
nothing = input()
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
result = 0
if len(arr) >= 4:
    result = pow(arr[3], 2)
print(result)
