numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers)):
    is_prime = True
    if numbers[i] > 1:
        for j in  range(2, int(numbers[i] ** 0.5)+1):
            if (numbers[i] % j) == 0:
                is_prime = False
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print(f'Primes {primes} \n Not primes {not_primes}')