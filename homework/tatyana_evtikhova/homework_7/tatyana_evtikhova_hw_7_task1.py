number = 13

while True:
    user_input = int(input("Введите предполагаемую цифру: "))

    if user_input == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
