'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001-st prime number?
-------------------------------------
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?
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


threshold = 1001
number = 2
primes = []

while len(primes) <= threshold:
    primes = [n for n in primes_method(number)]
    number += 1

result_text = "1001-st prime number = " + str(primes[threshold])

print(result_text)
