# Блок с вводом данных и преобразованию его в список#
array = list(map(int, input('Введите числа через пробел: ').split()))
some_num = int(input('Введите любое число, которое больше минимального и меньше максимального чисел из списка: '))

while some_num:
    if some_num < min(array):
        print('Вы ввели неверное значение, введите число больше минимального числа из списка')
        some_num = int(input('Введите любое число, которое больше минимального и меньше максимального чисел из списка: '))
    elif some_num > max(array):
        print('Вы ввели неверное значение, введите число меньше максимального числа из списка')
        some_num = int(input('Введите любое число, которое больше минимального и меньше максимального чисел из списка: '))
    else:
        break

# Функция по сортировке списка#
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array
array_sorted = qsort(array, 0, len(array) - 1)
print('Отсортированный список:')
print(array_sorted)

# Алгоритм двоичного поиска #
def binary_search(array_sorted, some_num, left, right):
    if left <= right:
        middle = (right + left) // 2
        if array_sorted[middle] < some_num and array_sorted[middle + 1] >= some_num:
            return middle
        elif some_num < array_sorted[middle]:
            return binary_search(array_sorted, some_num, left, middle - 1)
        else:
            return binary_search(array_sorted, some_num, middle + 1, right)
        return
    return False
print('Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу: ')
print(binary_search(array_sorted, some_num, 0, len(array_sorted) - 1))
