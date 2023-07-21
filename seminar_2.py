from random import choice, randint # для выпадения случайной монетки и случайного числа
from math import sqrt, pow # для извлечения корня из дискриминанта и возведения в степень

def heads_or_tails(n: int) -> [bool]:
    # сформируем массив с монетками(True - решки, False - орлы)
    result = [choice([True, False]) for i in range(n)]
    return result


def get_min_coins(coins: [bool]) -> int:
    heads = 0
    tails = 0
    for element in coins:
        if element:
            heads += 1
        else:
            tails += 1
    if heads > tails:
        return tails
    else:
        return heads


def get_x_y_list(total: int, prod: int) -> [int]:
    x = (total + sqrt(total**2 - 4 * prod))/2 # МотЕМотеКа
    y = total - x
    return [int(x), int(y)]


def exercise_10() -> None:
    """Задача 10: На столе лежат n монеток.
    Некоторые из них лежат вверх решкой, а некоторые – гербом.
     Определите минимальное число монеток, которые нужно перевернуть,
      чтобы все монетки были повернуты вверх одной и той же стороной.
       Выведите минимальное количество монет, которые нужно перевернуть"""
    print("задача 10")
    coins_quantuty = int(input("Введите количество монеток на столе "))
    coins = heads_or_tails(coins_quantuty)  # получим массив монеток
    print(coins)  # выведем массив с монетками
    print(f"Нужно перевернуть {get_min_coins(coins)} монеток")
    print()


def exercise_12() -> None:
    """Задача 12: Петя и Катя – брат и сестра.
    Петя – студент, а Катя – школьница.
    Петя помогает Кате по математике.
    Он задумывает два натуральных числа X и Y (X,Y≤1000),
    а Катя должна их отгадать. Для этого Петя делает две подсказки.
    Он называет сумму этих чисел S и их произведение P.
    Помогите Кате отгадать задуманные Петей числа."""
    print("задача 12")
    # зададим числа случайным образом
    x = randint(0, 1000)
    y = randint(0, 1000)
    total = x + y
    prod = x * y
    print(f"Сумма чисел {total}, произведение чисел {prod}")
    x,y = get_x_y_list(total, prod)
    print(f"Первое число равно {x}, второе число равно {y}")
    print()


def exercise_14() -> None:
    """Задача 14: Требуется вывести все целые степени двойки
    (т.е. числа вида 2^k), не превосходящие числа N."""
    print("задача 3")
    n = int(input("Введите число "))
    k = 0 # это степень
    number = 2
    result = 0
    flag = True
    print(f"Степени {number} меньше {n}")
    while (flag):
        result = number ** k
        if result < n:
            print(result, end = ' ')
        else:
            flag = False
        k += 1
    print()

if __name__ == "__main__":
    exercise_10()
    exercise_12()
    exercise_14()
