#Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все целые степени числа A от 1 до N.
A = input("Введите число A: ") #проверка чисел
while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print("Неправильно ввели!")
        A = input("Введите число A: ")
N = input("Введите степень N: ")
while type(N) != int:
    try:
        N = int(N)
        if N < 0: #проверка условия
            print("степень должна быть больше нуля")
            N = input("Введите степень N: ")
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите степень N: ")
i = 1
Z=1
while Z<=N:
    i*=A
    print(i)
    Z+=1
