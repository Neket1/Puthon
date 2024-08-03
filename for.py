numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] % 1 == numbers[i] & numbers[i] % numbers[j] == 0:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('primes', primes)
print('not_primes', not_primes)
"""
    print('primes', numbers[i])
"""