'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
---------------------------
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
'''


number = 2**1000
digits = [int(d) for d in str(number)]
digits_sum = sum(digits)

print("Initial number: " + str(number))
print("Digits: " + str(digits))
print("Sum of digits = " + str(digits_sum))