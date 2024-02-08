import sys

sys.set_int_max_str_digits(0)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_number(n):
    global result
    fib_gen = fibonacci_generator()
    for _ in range(n):
        result = next(fib_gen)
    return result


print(fibonacci_number(5))
print(fibonacci_number(200))
print(fibonacci_number(1000))
print(fibonacci_number(100000))
