# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 0,56 -> 11 

sum = 0
input_num = input('Введите число: ')

for el in input_num:
    if el.isdigit():
        sum += int(el)
print(sum)