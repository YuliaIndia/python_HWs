# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# num = int(input('Введите количество монет на столе --> ' ))
# coins = str(input('Введите с помощью 1 для орла и 0 для решки, как лежат монетки --> ' ))
# coins = coins[:num]
# orly = 0
# reshki = 0
# for i in range(num):
#     if coins[i:i+1]=='1':
#         orly+=1
#     else: reshki+=1
#     i+=1
# print('нужно перевернуть минимум ', (orly if orly<=reshki else reshki), 'монет')

# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
# две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# num1 = int(input('введите число 1 (от 1 до 1000): '))
# num2 = int(input('введите число 2 (от 1 до 1000): '))
# for x in range(num1):
#     for y in range(num1):
#         if x+y==num1 and x*y==num2:
#             print('x: ', x, ', y: ', y)
# else:
#     print('для такой пары нет решения')

# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

# num = int(input('введите число N: '))
# list2k=[]
# for i in range(num):
#     if 2**i<=num:
#         list2k.append(2**i)
# print(list2k)