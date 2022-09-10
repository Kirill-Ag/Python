# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
import random
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ

# функция настроек
def nastroyki():
    print('ИГРА "НАПЕРСТКИ"')
    print()
    print('Автор: Агапов Кирилл')
    print()
    print('Версия 1.10')
    print()
    print('Введи сколько у игрока денег')
    dengi = input()
    while True:
        if dengi.isdigit:
            dengi = int(dengi)   
            break
        else:
            print('Введите размер минимальной ставки')
            dengi = input()

    print('Введите размер минимальной ставки')
    minStavka = input()
    while True:
        if minStavka.isdigit():
            minStavka = int(minStavka)
            break
        else:
            print('Надо вводить только цифры')
            minStavka = input()

    return [dengi,minStavka]

def intro():
    print('''    Вы приходите на рынок

    На рынке вы видите человека сидящего за столом.

    Перед ним три наперстка и маленький шарик.

    Заинтерешсовавмись, вы подходите к человеку.

    Он предлагает вам испытать свою удачу
    и сыграть с ним на деньги''')

def proverka(dengi,minStavka):
    print('Сделайте вашу ставку')
    stavka = input()
    while True:
        if stavka.isdigit():
            #переводи строку в число
            stavka = int(stavka)
            #проверяем, что ставка больше минимальной
            if stavka > minStavka:
                #проверяем, что ставка меньше количества денег у игрока
                if stavka > dengi:
                    print('Ставка не может быть больше суммы денег у игрока')
                    stavka = input()
                else:
                    break
            else:
                break
        else:
            print('Ставка не может быть меньше минимальной')
            stavka = input()
    else:
        print('Надо вводить только цифры')
        stavka = input()
    return stavka

def sravnenie(game,igrok):
    if game == igrok:
        sovpadenie = True
    else:
        sovpadenie = False
    return sovpadenie

def intro2():
    print('''   После сделанной вами ставки
    ведущий начинает с большой скоростью перемещать
    наперстки по столу.
    
    Остановившись, он предлагает вам выбрать наперсток под которым,
    как вы думаете находится шарик.''')

def otvet():
    print('Введи номер наперстка:')
    nap = input()
    while True:
        if nap.isdigit():
            if (nap in '123') and (len(nap)==1):
                nap = int(nap)
                break
            else:
                print('Надо вводить цифры.')
            nap = input()
        return nap            


def playAgain():
    # создаем бесконечный цикл
    while True:
        # задаем вопос и получаем ответ
        print('Хотите продолжить играть? Да или нет.')
        otv = input()
        otv = otv.lower()
        # проверяем на совпадение со следующими фразами
        # "да", "Да", "ДА", "д", "y", "yes", "YES"
        # если есть совпадение то переменной присваеваем значение True
        # и прерываем цикл командой return
        if(otv == 'да') or (otv == 'да') or (otv == 'y') or (otv == 'yes'):
            return True
        # проверяем ответ на совпадение со следующими фразами
        # "нет", "Нет", "НЕТ", "н", "n", "no", "NO"
        # если есть совпадение то переменной присваеваем значение False
        # прерываем цикл командой return
        elif(otv == 'нет') or (otv == 'н') or (otv == 'n') or (otv == 'no'):
            return False
        # если совпадение с первыми двумя случаями нет
        # говорим пользавателю, что непоняли его ответа
        else:
            print('Я не понял ответ')                   

# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
many,minBig = nastroyki()
intro()

stavkaIgroka = proverka(many,minBig)
intro2()
napG = random.randint(1,3)
napI = otvet()
if sravnenie(napG,napI):
    print('Поздравляю! Ты выиграл!')
    many = many + stavkaIgroka
else:
    print('Увы! Ты проиграл!')
    many = many + stavkaIgroka

print(many)            