def enumeratePrimes(n):
    if n <= 1:
        return []
    primes = []
    for i in range(2, n):
        divider = next((j for j in range(2, i) if i % j == 0), None)
        is_prime = divider is None

        if is_prime:
            primes.append(i)
    return primes


print(enumeratePrimes(30))