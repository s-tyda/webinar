def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


N = int(input())
result = number_to_base(N, 5)
for x in result:
    print(2*x, end='')
