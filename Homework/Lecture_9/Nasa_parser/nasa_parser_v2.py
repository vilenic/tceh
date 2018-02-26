#!/usr/bin/python3

import re
import sys
import time


#def parser(filename):
#    """Тот же функционал, только без использования регулярных выражений"""
#
#    parsed_values = {}
#    with open(data_file, 'r') as f:
#        for l in f:
#            value = l.split('\t')[5]
#
#            if value not in parsed_values.keys():
#                parsed_values[value] = 1
#            else:
#                parsed_values[value] += 1
#    return parsed_values

def get_time(value):
    value = time.gmtime(value)
    day = value[2]
    month = value[1]
    year = value[0]
    date = '{}.{}.{}'.format(day, month, year)
    return date

def parserRegex(filename, mode):
    parsed_values = {}
    with open(filename) as file:
        for line in file:
            if mode == 'http':
                value = re.search(r'(?P<http_code>\s[1-5]\d\d\s)', line)
                if value:
                    value = value.group(0)
                    value = value.strip('\t')
            elif mode == 'date':
                value = re.search(r'(?:(8\d{8}))', line)
                if value:
                    value = value.group(0)
                    value = get_time(int(value))
            elif mode == 'url':
                value = re.search(r'(?:/\S*)', line)
                if value:
                    value = value.group(0)

            if value:
                if value not in parsed_values.keys():
                    parsed_values[value] = 1
                else:
                    parsed_values[value] += 1
            else:
                continue

    return parsed_values

def top10(dictionary):
    """Берет словарь и преобразует его в сортированный (в обратном порядке,
    по второму значению в элементе списка) список с выводом первых 10
    индексов или соответствующего количества индексов"""
    list_of_counted = []
    for k, v in dictionary.items():
        list_of_counted.append((k, v))

    list_of_counted = sorted(list_of_counted, \
            key=lambda url: url[1], reverse=True)
    length = len(dictionary)
    if length >= 20:
        for i in range(20):
            print(list_of_counted[i][0], list_of_counted[i][1])
    else:
        for i in range(length):
            print(list_of_counted[i][0], list_of_counted[i][1])

def print_result(data, header):
    times = len(header)
    print()
    print('*' * times)
    print(header + '\n')
    top10(data)
    print('-' * times)

if __name__ == '__main__':

    data = 'nasa.tsv'

    nasa_data_http = parserRegex(data, 'http')
    print_result(nasa_data_http, 'HTTP codes list:')
    time.sleep(1)

    nasa_data_date = parserRegex(data, 'date')
    print_result(nasa_data_date, 'Date list:')
    time.sleep(1)

    nasa_data_url = parserRegex(data, 'url')
    print_result(nasa_data_url, 'URL list:')
