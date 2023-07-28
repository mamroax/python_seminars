def exercise_25() -> None:
    """Напишите программу, которая принимает на вход
    строку, и отслеживает, сколько раз каждый символ
    уже встречался. Количество повторов добавляется к
    символам с помощью постфикса формата _n.
    Input: a a a b c a a d c d d
    Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"""
    dir1 = {}  # создаем пустой словарь
    for i in input("Введите строку ").split():
        if i in dir1.keys():
            dir1[i] = dir1.get(i) + 1
            print(f"{i}_{dir1[i]}", end=" ")
        else:
            dir1.update({i: 0})
            print(i, end=" ")


def exercise_27() -> None:
    """Пользователь вводит текст(строка). Словом считается
    последовательность непробельных символов идущих
    подряд, слова разделены одним или большим числом
    пробелов. Определите, сколько различных слов
    содержится в этом тексте.
    Input: She sells sea shells on the sea shore The shells
    that she sells are sea shells I'm sure.So if she sells sea
    shells on the sea shore I'm sure that the shells are sea
    shore shells
    Output: 13"""
    dir1 = {}  # создаем пустой словарь
    for i in input("Введите строку ").split():
        if i.lower() not in dir1.keys():
            dir1.update({i.lower(): 0})
    print()
    print(len(dir1.keys()))


def exercise_29():
    """Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам."""
    flag = True
    numbers = []
    while (flag):
        number = int(input())
        numbers.append(number)
        if number <= 0:
            flag = False
            print(max(numbers))


# exercise_25()
# exercise_27()
exercise_29()
