numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        primes.append(numbers[i])
    elif numbers[i] % 2 != 0:
        not_primes.append(numbers[i])

print('primes', primes)
print('not_primes', not_primes)