#Дана строка. Преобразовать в ней все прописные латинские буквы в строчные
s = input("Введите строку: ")
result = s

for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    result = result.replace(ch, ch.lower())

print(result)