from math import pi

def exercise_47() -> None:
    """Задача №47
    У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
    программы используется множество раз и вы не хотите ничего сломать):
    transformation = <???>
    values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
    transormed_values = list(map(transformation, values))
    Единственный способ вашего взаимодействия с этим кодом - посредством задания
    функции transformation.
    Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
    список значений, а нужно получить его как есть.
    Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
    копией values."""
    values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print(values)
    transformation = lambda x: x
    transormed_values = list(map(transformation, values))
    print(transormed_values)


def exercise_49():
    """Задача №49. Решение в группах
    Планеты вращаются вокруг звезд по эллиптическим орбитам.
    Назовем самой далекой планетой ту, орбита которой имеет
    самую большую площадь. Напишите функцию
    find_farthest_orbit(list_of_orbits), которая среди списка орбит
    планет найдет ту, по которой вращается самая далекая
    планета. Круговые орбиты не учитывайте: вы знаете, что у
    вашей звезды таких планет нет, зато искусственные спутники
    были были запущены на круговые орбиты. Результатом
    функции должен быть кортеж, содержащий длины полуосей
    эллипса орбиты самой далекой планеты. Каждая орбита
    представляет из себя кортеж из пары чисел - полуосей ее
    эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
    где a и b - длины полуосей эллипса. При решении задачи
    используйте списочные выражения. Подсказка: проще всего
    будет найти эллипс в два шага: сначала вычислить самую
    большую площадь эллипса, а затем найти и сам эллипс,
    имеющий такую площадь. Гарантируется, что самая далекая
    планета ровно одна
    """
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    print(find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits: [tuple]) -> (float, float):
    # filtered = list(filter(lambda x: x[0] != x[1], list_of_orbits))  # отфильтровали
    # orbit_squares = list(map(lambda x: pi * x[0] * x[1], filtered))  # нашли площади орбит
    # maxim = max(orbit_squares)  # вычислили самую большую площадь эллипса
    # max_index = orbit_squares.index(maxim)  # нашли индекс самой большой площади эллипса
    # return list_of_orbits[max_index]  # вывели характеристики орбиты с максимальной площадью
    filtered_orbits = [pi * i[0] * i[1] for i in list_of_orbits if i[0] != i[1]] # использовал списочное выражение
    maxim = max(filtered_orbits)
    max_index = filtered_orbits.index(maxim)
    return list_of_orbits[max_index]


# exercise_49()

def exercise_51():
    """Задача №51. Решение в группах
    Напишите функцию same_by(characteristic, objects), которая
    проверяет, все ли объекты имеют одинаковое значение
    некоторой характеристики, и возвращают True, если это так.
    Если значение характеристики для разных объектов
    отличается - то False. Для пустого набора объектов, функция
    должна возвращать True. Аргумент characteristic - это
    функция, которая принимает объект и вычисляет его
    характеристику.
    """
    list1 = []
    print(same_by(lambda i: i % 2 == 0, list1)) # проверяет, все ли элементы чётные

def same_by(characteristic, objects):
    for object in objects:
        if not characteristic(object):
            return False
    return True


exercise_51()

# exercise_47()
# exercise_49()
# exercise_51()

def exercise_55():
    """Дан список, вывести в отдельном списке буквы, а в другом цифры, используя фильтр
     ["asd", 1, 2,"gfd"]
     ["asd","gfd"][1,2]
     """
    list1 = ["a", "b", "c", 1, 2, 3]
    list2 = list(filter(lambda x: isinstance(x, str), list1))
    list3 = list(filter(lambda x: isinstance(x, int), list1))
    print(list2)
    print(list3)


# exercise_55()

def exercise_57() -> None:
    """Дано вещественное число, показать сумму его цифр
    3.12, 6"""
    number = 3.1222 # float
    num_str = str(number) #
    splited_str = num_str.replace(".", "") # 312
    result = sum(map(lambda x: int(x), splited_str)) # result = sum([int(i) for i in splited]) то же самое
    print(result)
    # print(sum(map(lambda x: int(x), str(number).replace(".", "")))) # ["3", "12"]


# exercise_57()

def exercise_59():
    """3) Дан список целых чисел, оставить в нём только двузначные числа"""
    list1 = [1, 2, 3, 4, 23, 34]
    print(list(filter(lambda x: x in range(10, 99), list1)))

# exercise_59()
