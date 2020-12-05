nothing = input()
arr = list(map(int, input().split()))
up = True
result = 1
for i in range(len(arr)-1):
    if up and arr[i+1] < arr[i]:
        up = False
        result += 1
    elif not up and arr[i+1] > arr[i]:
        up = True
        result += 1
print(result)
