'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
-----------------------------------------
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
'''


def primes_method(n):
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p] and sieve[p] % 2 == 1):
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


number = 2000000
primes = [n for n in primes_method(number)]
sum_p = sum(primes)

print("Sum of primes less than 2M = " + "{:,}".format(sum_p))
