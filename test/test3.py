def draw_horizontal_line(length, char="-"):
    """Функция для отрисовки горизонтальной линии"""
    print(char * length)


def draw_vertical_line(length, char="|"):
    """Функция для отрисовки вертикальной линии (пустой строки с рамками по краям)"""
    # Печатаем символ, пробелы (на длину текста) и снова символ
    print(char)


def frame_word(word):
    """Функция, собирающая слово в рамку"""
    # Длина рамки = длина слова + 4 (по одному пробелу с каждой стороны + 2 символа рамки)
    frame_length = len(word) + 4

    draw_horizontal_line(frame_length, "*")  # Верхняя граница
    print("*", word, "*")  # Слово в рамке
    draw_horizontal_line(frame_length, "*")  # Нижняя граница


# Основная программа
user_word = input("Введите слово для рамки: ")
frame_word(user_word)