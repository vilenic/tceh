#!/usr/bin/python3

# Эта часть для большей наглядности при
# необходимости добавить вопросы
# и видеть их порядок
question_0 = "Введите значение числа Пи: "
answers_0 = ["3.14", "3,14"]

question_1 = "Имя автора языка Python: "
answers_1 = [
    "гвидо",
    "гвидо ван россум",
    "гвидо ван росум",
    "guido van rossum",
    "guido",

]

question_2 = "Температура тройной точки воды (в градусах Цельсия): "
answers_2 = ["0.01", "0,01"]

questions = [
    question_0,
    question_1,
    question_2,

]

answers = [
    answers_0,
    answers_1,
    answers_2,

]

print('\nДля досрочного завершения работы введите "exit"\n')

index = 0
numberOfQuestions = len(questions) - 1

while index <= numberOfQuestions:
    print("Вопрос #" + str(index + 1))
    user_input = input(questions[index] + "\n\n")
    if user_input.lower() in answers[index]:
        print("\nОтлично!\n")
        index += 1
        continue
    elif user_input.lower() == "exit":
        if input("Вы уверенны? (y/n)\n") == "y":
            break
        else:
            continue
    else:
        print("\nВы допустили ошибку! Пробуем еще раз.\n")
        continue

# Поздравляем только если получены правильные ответы
# на все три вопроса
if index == 3:
    greeting = "+ Поздравляем с успешным выполнением заданий! Удачи! +"
    print("+" * len(greeting))
    print(greeting)
    print("+" * len(greeting))
    print("")

