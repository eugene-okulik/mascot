import sys

sys.set_int_max_str_digits(0)


def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


fibonacci_numbers = list(fib(100001))

print(fibonacci_numbers[5])
print(fibonacci_numbers[200])
print(fibonacci_numbers[1000])
print(fibonacci_numbers[100000])
