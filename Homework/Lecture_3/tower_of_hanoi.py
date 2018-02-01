#!/usr/bin/python3


def solveHanoi(discs, source, target, buffer, step):
    """Решение головоломки с заменой аргументов внутри рукурсии"""

    if discs == 1:

        print("Перекладываем {} диск с {} стрежня на {}\n".format(discs, source, target))
        step += 1

        return step

    else:

        step = solveHanoi(discs - 1, source, buffer, target, step)

        print("Перекладываем {} диск с {} стрежня на {}\n".format(discs, source, target))
        step += 1

        step = solveHanoi(discs - 1, buffer, target, source, step)

        return step

def main():

    moves = 0
    sourcelist = 1
    bufferlist = 2
    targetlist = 3
    numberdiscs = int(input("Введите количество дисков: \n"))

    print()
    print("Ожидаемое количество ходов:", 2 ** numberdiscs - 1, "\n")
    moves = solveHanoi(numberdiscs, sourcelist, targetlist, bufferlist, moves)
    print("Фактическое количество ходов: {}".format(moves))

if __name__ == '__main__':
    main()
