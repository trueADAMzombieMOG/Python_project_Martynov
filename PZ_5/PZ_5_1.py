def draw_horizontal_line(length, symbol="-"):
    print(symbol * length)

def frame_word(word):
    frame_length = len(word) + 4

    draw_horizontal_line(frame_length, "-")  # Верхняя граница
    print("|", word, "|")  # Слово в рамке
    draw_horizontal_line(frame_length, "-")  # Нижняя граница

user_word = input("Введите слово для рамки: ")
frame_word(user_word)