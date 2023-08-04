# kek = lambda a: (a, a ** 2)
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list2 = [kek(i) for i in list1 if i % 2==0]
# print(list2)

def select(f, col): # то же, что и встроенная функция map
    return [f(x) for x in col]

def where(f, col): # то же, что и встроенная функция filter
    return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# list_1 = [x for x in range(1,20)]
# print(list_1)
#
# list_1 = [map(lambda x: x+10, list_1)]
# print(list_1)

list1 = [12, 23, 15, 25, 50, 265]
res = list(filter(lambda x: x % 10 == 5, list1))
print(res)
