def fib(n: int) -> list[int]:
    if n in [0, 1]:
        return 1
    return fib(n - 2) + fib(n - 1)


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([14, 5, 4, 23, 34, 23, 34, 23, 1, 2, 3]))

# n = 10
# list1 = []
# for i in range(n):
#     list1.append(fib(i))
# print(*list1)
