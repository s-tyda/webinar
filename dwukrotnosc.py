def digit_sum(n):
    result = 0
    while n != 0:
        result += n % 10
        n //= 10
    return result


(N, X) = list(map(int, input().split()))
seq = [0, X]
index = {X: 1}
result = 0
for i in range(2, N+1):
    seq.append(2 * digit_sum(seq[-1]))

    # Zaczął się cykl
    if seq[-1] in index.keys():
        start = index[seq[-1]]
        end = i
        length = end - start
        idx = (N - start) % length
        result = seq[start + idx]
        break

    index[seq[-1]] = i
    result = seq[i]

print(result)
