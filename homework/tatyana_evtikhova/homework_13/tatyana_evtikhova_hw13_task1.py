import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_file_path, 'r') as file:
    lines = file.readlines()


def process_action(action, date):
    if "распечатать эту дату, но на неделю позже" in action:
        new_date = date + timedelta(weeks=1)
        print(new_date.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif "распечатать какой это будет день недели" in action:
        print(date.strftime('%A'))
    elif "распечатать сколько дней назад была эта дата" in action:
        today = datetime.now()
        days_difference = (today - date).days
        print(days_difference)

for line in lines:
    parts = line.split(" - ")
    date_str = parts[0].split('. ')[1]
    action = parts[1].strip()
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    process_action(action, date)
