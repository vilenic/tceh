#!/usr/bin/python3

import re

def open_file(filename):
    with open(filename) as f:
        return f.read()



def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)
    print('Done writing to file {}'.format(filename))



def parseHttpCodes(data):
    http = {}

    for ix in range(1, 6):
        http["Code {}**: ".format(str(ix))] = len(re.findall(r'\s[1-5]\d\d\s'))
    return http



def print_result(data_dict, header):
    times = len(header)
    print('*' * times)
    print(header)
    print('*' * times)

    for k, v in data_dict.items():
        print(k, v)



if __name__ == '__main__':

    data_file = 'nasa.tsv'
#    data_file = input("Enter filename: ")

    nasa_data = open_file(data_file)

    http_codes = parseHttpCodes(nasa_data)
    print_result(http_codes, "HTTP statuses from log {}".format(data_file))
