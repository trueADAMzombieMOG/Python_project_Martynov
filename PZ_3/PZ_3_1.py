 # 1.Даны три целых числа: A, B, C. Проверить истинность высказывания: "Каждое из чисел A,B,C положительное".
A = input("Введите число A: ")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите число A: ")
B = input("Введите число B: ")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели!")
        B = input("Введите число B: ")
C = input("Введите число C: ")
while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print("Неправильно ввели!")
        C = input("Введите число C: ")

# Проверка условия
if A > 0 and B > 0 and C > 0:
    print("Истина: Все числа положительные!")
else:
    print("Ложь: Не все числа положительные")