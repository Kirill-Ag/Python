import random
# подключить модуль random
print('Привет, как тебя зовут?')
myName = input()
# Поздоровались, спросили имя, ответ в переменную myName
s = random.randint(1,20)
print('Я загадала число от 1 до 20.')
# программа загадала (сгенериловала) число от 1 до 20 и рассказалаоб этом игроку
for i in range(3):
    # даем игроку 3 попытки отгадать число
    print('Введи число от 1 до 20')
    y = input()
    # Программа просит ввести число и записывает введенное в переменную y
    y = int(y)
    # переводистроку в число
    if s > y:
        print('Твое число меньше загаданного')
    if s < y:
        print('Твое число больше загадонного')
    if s == y:
        Break
if s == y:
    print('Поздровляю! Ты выиграл.')
if s != y:
    print('Увы ты проиграл! Загадоннае число '+str(s))
