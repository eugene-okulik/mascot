temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

high_temperature = filter(lambda x: x > 28, temperatures)
high_temperature_list = list(high_temperature)

print(high_temperature_list)
print(max(high_temperature_list))
print(min(high_temperature_list))

average_temperature = sum(high_temperature_list) / len(high_temperature_list)

print(average_temperature)

# Округлим значение до более привычного

print(round(average_temperature))
