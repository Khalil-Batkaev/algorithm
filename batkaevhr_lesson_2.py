from random import randint

"""
Реализовать алгоритм пирамидальной сортировки (сортировка кучей).
"""


# Преобразование в двоичную кучу поддерева с корневым узлом idx
def heapify(array, length, idx):
    root_idx = idx
    left_idx = 2 * idx + 1
    right_idx = 2 * idx + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if left_idx < length and array[root_idx] < array[left_idx]:
        root_idx = left_idx
    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if right_idx < length and array[root_idx] < array[right_idx]:
        root_idx = right_idx

    # Меняем значение корня, если нашелся дочерний элемент больше и запускаем ещё раз с новым корнем
    if root_idx != idx:
        array[idx], array[root_idx] = array[root_idx], array[idx]
        heapify(array, length, root_idx)


def heap_sort(array):
    length = len(array)

    # Построение бинарной кучи (max-heap)
    for i in range(length, -1, -1):
        heapify(array, length, i)

    # Перемещаем текущий корень в конец массива, исключая его из сортировки и запускаем заново
    for i in range(length-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


MIN_ITEM = 0
MAX_ITEM = 100
SIZE = 25

data = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Неотсортированный массив: {data}')
heap_sort(data)
print(f'Отсортированный массив: {data}')
