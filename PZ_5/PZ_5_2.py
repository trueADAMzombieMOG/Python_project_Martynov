#Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг: значение A
# переходит в C, значение C — в B, значение B — в A. С помощью этой функции выполнить сдвиг для двух наборов чисел.
def ShiftLeft3(A, B, C):
    return B, C, A


for i in range(2):
    print(f"Набор {i + 1}:")
    A = (input("A = "))
    while type(A)!=int:
        try:
            A = int(A)
        except ValueError:
            print("введите корректное число")
            A = (input("A = "))
    B = (input("B = "))
    while type(B) != int:
        try:
            B = int(B)
        except ValueError:
            print("введите корректное число")
            B = (input("B = "))
    C = (input("C = "))
    while type(C) != int:
        try:
            C = int(C)
        except ValueError:
            print("введите корректное число")
            C = (input("C = "))
    print(ShiftLeft3(A, B, C))