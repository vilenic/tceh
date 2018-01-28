#!/usr/bin/python3

# Эта часть для большей наглядности при
# необходимости добавить вопросы
# и видеть их порядок

qa_dict = {
    "Введите значение числа Пи: " : ["3.14", "3,14"],
    "Имя автора языка Python: " : ["гвидо", "гвидо ван россум", "гвидо ван\
        росум", "guido van rossum", "guido",],
    "Температура тройной точки воды (в градусах Цельсия): " : ["0.01", "0,01"],
}

print('\nДля досрочного завершения работы введите "exit"\n')

correct_answers = 0

for k, v in qa_dict.items():
    while True:
        user_input = input(k + "\n")
        if user_input.lower() in v:
           correct_answers += 1
           print("\nОтлично!\n")
           break
        elif user_input.lower() == "exit":
            if input("Вы уверенны? (y/n)\n") in ["y", "yes"]:
                exit()
            else:
                continue
        else:
            print("\nВы допустили ошибку! Пробуем еще раз.\n")
            continue


# Поздравляем только если получены правильные ответы
# на все три вопроса
if correct_answers == len(qa_dict):
    greeting = "+ Поздравляем с успешным выполнением заданий! Удачи! +"
    print("+" * len(greeting))
    print(greeting)
    print("+" * len(greeting))
    print("")

