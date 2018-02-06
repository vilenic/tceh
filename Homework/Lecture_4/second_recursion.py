#!/usr/bin/python

import random

def sort_list(listtoSort):
    """Функция сортировки по методу "merge sort". Берет список, рекурсивно
    делит его пополам, пока длина больше 1, далее циклично соединяет
    отсортированные списки, замещая ими исходный (тот, с которым мы
    приходим в функцию)"""

    print("Делим пополам: ", listtoSort)

    if len(listtoSort) > 1:

        # Находим середину
        mid = len(listtoSort) // 2

        # Дробим список по центру
        left = listtoSort[:mid]
        right = listtoSort[mid:]

        # Отправляемся в рекурсию для обеих частей
        sort_list(left)
        sort_list(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            # Сравниваем и записываем элементы в результирующий массив, в
            # соответствии с итерируемым индексом
            if left[i] < right[j]:
                listtoSort[k] = left[i]
                i += 1

            else:
                listtoSort[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            listtoSort[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            listtoSort[k] = right[j]
            j += 1
            k += 1

    print("Соединяем: ", listtoSort)


def main():

    list_to_sort = []

    for n in range(1, 101):
        list_to_sort.append(n)

    random.shuffle(list_to_sort)

    sort_list(list_to_sort)
    print(list_to_sort)




if __name__ == '__main__':
    main()
