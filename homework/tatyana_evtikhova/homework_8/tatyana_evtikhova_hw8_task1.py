import random


def salary_counter(salary1, bonus1):
    if bonus1:
        random_bonus = random.randint(0, 10000)
        total_salary = salary1 + random_bonus
    else:
        total_salary = salary1
    return total_salary


salary = int(input('Введите Вашу зарплату: '))
bonus = random.choice([True, False])
result = salary_counter(salary, bonus)
print(result)
