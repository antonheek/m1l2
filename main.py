import random
import string
print("Генератор паролей")
len_str = int(input("Сколько символов вы хотите добавить в пароль? "))

passw = ""
for i in range(len_str):
        passw += random.choice(string.printable)
print(passw)
