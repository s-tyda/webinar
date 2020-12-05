def even_digits(n):
    if n == 0:
        return ''
    else:
        digit = n % 5
        even_digit = 2 * digit
        return even_digits(n//5) + str(even_digit)


N = int(input())
print(even_digits(N))
