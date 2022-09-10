# Это игра по угадыванью чисел
import random
# мы подключили модуль рандом к программе
print('Привет, как тебя зовут?')
myName = input()

while True:
    # поздоровались, спросили имя, игрок ввел свое имя
    print(myName+', я загадываю число от 1 до 20.')
    chislo = random.randint(1,20)
    # сказали игроку в каком диапазоне загадываем число и загадали его
    for i in range(3):
        #даем три попытки
        print('Попробуй отгадай. Введи число от 1 до 20')
        vybor = input()
        #проверяем, что игрок ввел число, если нет, то требуем еще раз ввести число
        while True:
            if vybor.isdigit():
                break
            else:
                print('Введи число.')
                vybor = input()

        vybor = int(vybor)
        # игрок ввел число, строку перевели в число и записали в переменную
        if chislo < vybor:
            print('Загаданное число больше')
        if chislo > vybor:
            print('Загадонное число меньше')
        if chislo == vybor:
            break
        # сравниваем числа, даем подсказку, прерываем попыткиесли игрок угадал число
        if chislo == vybor:
            print('Поздравляю! Ты отгадал число')
        if chislo != vybor:
            print('Увы! Загаданное число '+str(chislo))


        pr = True
        print('Ты хочешь попробоватьеще один раз?')
        otvet = input()
        if(otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            pr = False

        if pr:
            # игра прекращается
            break                                  