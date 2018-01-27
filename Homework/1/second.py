#!/usr/bin/python3

def isNumber(string):
    numbers = "0123456789"
    ops = "-+*/"
    num = 0
    op = 0
    char = 0
    for ch in string:
        if ch in numbers:
            num += 1
        elif ch in ops:
            op += 1
        elif ch == ".":
            continue
        else:
            char +=1
    if op == 0 and num >= 1 and char == 0:
        return True
    elif string[0] == "-" and num >= 1 and char == 0:
        return True
    elif op == 1 and num == 0 and char == 0:
        return False
    else:
        return ValueError

def mathOperation(total, sign, number):
    if sign == "+":
        total += number
    elif sign == "-":
        total -= number
    elif sign == "*":
        total *= number
    elif sign == "/":
        total /= number
    return total

def main():
    running_total = 0
    operation = 0
    while True:
        try:
            user_input_1 = input("Введите число: ")
            if user_input_1 == "":
                user_input_exit = input("Вы уверены? (y/n): ")
                if user_input_exit == "y":
                    exit()
                else:
                    continue
            elif isNumber(user_input_1):
                running_total = float(user_input_1)
                break
            elif isNumber(user_input_1):
                print("Нужно начать с числа!")
                continue
        except ValueError:
            print("Проверьте корректность ввода")
    while True:
        try:
            user_input_2 = input("Введите следующее действие или число: ")
            if user_input_2 == "":
                user_input_exit = input("Вы уверены? (y/n): ")
                if user_input_exit == "y":
                    exit()
                else:
                    continue
            elif isNumber(user_input_2) and operation == 0:
                print("Сначала введите действие!")
                continue
            elif isNumber(user_input_2) is False:
                operation = user_input_2
                continue
            else:
                user_input_2 = float(user_input_2)
                running_total = mathOperation(running_total, operation,\
                        user_input_2)
        except ValueError:
            print("Проверьте корректность ввода")
            continue
        except ZeroDivisionError:
            print("Деление на ноль!!!")
            continue
        print("")
        # Если число дробное
        if (running_total % 1) > 0:
                print("Промежуточный итог: {:.2f}".format(running_total))
        # Если целое
        else:
            print("Промежуточный итог: ", int(running_total))
        # Решил оставить, хотя эффект не по задумке изначально: в силу
        # записи символа операции в переменную, есть возможность не
        # вводить каждый раз новый символ, а вести последовательный
        # расчет суммы, к примеру
        print("Текущий символ следующей операции: ", operation)
        print("")
        continue
main()



