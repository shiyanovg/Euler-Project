'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

--------------------------------
Сумма квадратов первых десяти натуральных чисел равна

1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
'''

threshold = 10
n = 1
first100nat = []
while n < threshold+1:
    first100nat.append(n)
    n += 1


print(first100nat)
