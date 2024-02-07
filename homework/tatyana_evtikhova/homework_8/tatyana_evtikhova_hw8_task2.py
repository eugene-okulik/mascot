import sys

sys.set_int_max_str_digits(0)


def fibonacci_number(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibonacci_number(5))
print(fibonacci_number(200))
print(fibonacci_number(1000))
print(fibonacci_number(100000))
