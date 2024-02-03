def number_in_strings(results):
    for result in results:
        number = result.split()[-1]
        add_number = int(number) + 10
        print(add_number)


result42 = "результат операции: 42"
result54 = "результат операции: 54"
result209 = "результат работы программы: 209"
result2 = "результат: 2"

number_in_strings([result42, result54, result209, result2])
