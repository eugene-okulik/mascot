def decorator(func):
    def wrapper(first, second, operation):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = calc(num1, num2, None)
print(result)
