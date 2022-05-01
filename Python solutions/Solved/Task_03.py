'''

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

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


number = 86756 #600851475143
denums = [n for n in primes_method(number) if number % n == 0]


final_text = "The largest prime factor = " + str(max(denums))


print("List of prime deviders: " + str(denums))

print(final_text)
