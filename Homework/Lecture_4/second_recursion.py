#!/usr/bin/python

import random

#Написать алгоритм, который сортирует список по следующему алгоритму:
#Сортируемый массив разбивается на две части примерно одинакового размера;
#Каждая из получившихся частей сортируется отдельно, например — тем же самым алгоритмом;
#Два упорядоченных массива половинного размера соединяются в один.
#1.1. — 2.1. Рекурсивное разбиение задачи на меньшие происходит до тех пор, пока размер массива не достигнет единицы (любой массив длины 1 можно считать упорядоченным).
#3.1. Соединение двух упорядоченных массивов в один.
#Основную идею слияния двух отсортированных массивов можно объяснить на следующем примере. Пусть мы имеем два уже отсортированных по неубыванию подмассива. Тогда:
#3.2. Слияние двух подмассивов в третий результирующий массив.
#На каждом шаге мы берём меньший из двух первых элементов подмассивов и записываем его в результирующий массив. Счётчики номеров элементов результирующего массива и подмассива, из которого был взят элемент, увеличиваем на 1.
#3.3. «Прицепление» остатка.
#Когда один из подмассивов закончился, мы добавляем все оставшиеся элементы второго подмассива в результирующий массив.

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
