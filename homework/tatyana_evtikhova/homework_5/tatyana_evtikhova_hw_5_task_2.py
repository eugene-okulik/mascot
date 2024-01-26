result42 = "результат операции: 42"
result514 = "результат операции: 514"
result9 = "результат работы программы: 9"

number42 = int(result42[result42.index(':') + 2:]) + 10
number514 = int(result514[result514.index(':') + 2:]) + 10
number9 = int(result9[result9.index(':') + 2:]) + 10
print(number42)
print(number514)
print(number9)
