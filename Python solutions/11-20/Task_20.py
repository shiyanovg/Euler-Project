'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
-----------------------------------
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
'''

number = 100
factorial = 1
factorial_list = []
i = 1

while i <= number:
    factorial_list.append(i)
    factorial *= i
    i+=1

factorial_string = str(factorial)

print("List of Numbers: " + str(factorial_list))

print("Factorial of Numbers = " + str(factorial))

list2 = [int(d) for d in str(factorial)]

print("Numbers in factorial: " + str(list2))

num_sum = sum(list2)

print("Sum of factorial numbers = " + str(num_sum))
