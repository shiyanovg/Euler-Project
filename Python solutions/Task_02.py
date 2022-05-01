'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
------------------------------------------------------------
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''

treshold = 4000000

fib_start = [1, 2]
fib = fib_start
# fib_even = []

# Fill fibonachy list
while (fib[-1] < treshold) & (sum(fib[-2:]) < treshold):
    fib.append(sum(fib[-2:]))


fib_even = [n for n in fib if n % 2 == 0]

final_sum = sum(fib_even)

result_text = "Final sum = " + "{:,}".format(final_sum)

print(result_text)