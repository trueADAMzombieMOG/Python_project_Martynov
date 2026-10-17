# 2. Дано челое число. Вывести его строку-описание вида "отрицательное четное число","положительное нечетное число" итд
number = input("введите число для анализа:")
while type(number) != int:
    try:
        number = int(number)

    except ValueError:
        print("ошибка, Введите число")
        number = (input("введите число для анализа:"))

if number == 0:
    print("нулевое число")
elif number > 0 and number % 2 == 0:
    print("положительное четное число")
elif number > 0 and number % 2 != 0:
    print("положительное нечетное число")
elif number < 0 and number % 2 == 0:
    print("отрицательное четное число")
elif number < 0 and number % 2 != 0:
    print("отрицательное нечетное число")