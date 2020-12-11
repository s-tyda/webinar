houses = int(input())
candies = list(map(int, input().split()))
result = 0

for L in range(houses):
    for R in range(L, houses):
        sum = 0
        for i in range(L, R+1):
            sum += candies[i]
        if sum % 2 == 0:
            result += 1

print(result)

result = 0
for L in range(houses):
    sum = 0
    for R in range(L, houses):
        sum += candies[R]
        if sum % 2 == 0:
            result += 1

print(result)

result = 0
sum = 0
evens = 1
odds = 0

for candy in candies:
    sum += candy
    if sum % 2 == 0:
        result += evens
        evens += 1
    else:
        result += odds
        odds += 1

print(result)
