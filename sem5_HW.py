# Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def step(a,b):
#     if b==0:
#         return 1
#     return step(a,(b-1))*a
# num1=int(input('введите число-основание: '))
# num2=int(input('введите число-степень: '))
# print(f'{num1} в степени {num2} = {step(num1,num2)}')

# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summ_rekurs(a,b):
    sum=a
    if b==0:
        return sum
    return summ_rekurs(a,b-1)+1
num1=int(input('введите число1: '))
num2=int(input('введите число2: '))
print(f'{num1} + {num2} = {summ_rekurs(num1,num2)}')

