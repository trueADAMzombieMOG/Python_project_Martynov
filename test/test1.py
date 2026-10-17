A = input("введите целый отрезок")
while type (A) != int:
    try:
        A=int(A)
    except ValueError:
        print("ошибка, введите корректные числа")
        A = input("введите целый отрезок")

B = input("введите отрезок от целого")
while type (B) != int:
    try:
        B=int(B)
    except ValueError:
        print("ошибка, введите корректные числа")
        B = input("введите отрезок от целого")

if A > B:
    print("result=", A // B)
else:
    print("ошибка, малый отрезок больше целого")