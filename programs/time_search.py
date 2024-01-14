#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit  # импорт модуля для измерения времени


def search(list_search, desired_value):
    """
    Функция поиска заданного значения в переданном ей списке списке.
    """
    for i in list_search:
        if desired_value == i:
            break
    return None


if __name__ == '__main__':
    # Необходимо проанализировать скорость нахождения элемента в зависимости от его положения в списке
    # методом линейного поиска. Необходимо рассмотреть два случая нахождения элемента в списке:
    # - средний случай (элемент находится в середине списка);
    # - худший случай (элемент находится в конце списка).
    # Заполним списки известными целыми значениями в заданном диапазоне, тогда элемент находящийся в
    # середине будет равен половине диапазона, а элемент, которого нет в списке будет отрицательного значения.

    current_list = [i for i in range(1, 100001)]

    # Для записи результатов используются два файла в той же директории, что и данный модуль.
    filename_average = 'average_case.txt'
    filename_worst = 'worst_case.txt'

    # Получим данные при поиске элемента в списке в среднем случае.
    for number in range(0, 400):

        # Получим данные при поиске элемента в списке в среднем случае.
        middle_element = len(current_list) / 2
        with open(filename_average, 'a') as file:
            time_search = timeit.timeit(lambda: search(current_list, middle_element), number=10)
            file.write(str(time_search) + '\n')
        file.close()

        # Получим данные при поиске элемента в списке в худшем случае.
        last_element = -10  # Таких элементов нет в списке
        with open(filename_worst, 'a') as file:
            time_search = timeit.timeit(lambda: search(current_list, last_element), number=10)
            file.write(str(time_search) + '\n')
        file.close()

        # Увеличим размер данного списка.
        for i in range(1, 1001):
            current_list.append(current_list[-1] + 1)
