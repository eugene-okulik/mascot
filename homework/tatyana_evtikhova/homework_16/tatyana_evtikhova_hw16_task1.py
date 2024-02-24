import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()
data = []

with open(eugene_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    next(file_data)
    for row in file_data:
        name = row[0]
        second_name = row[1]
        group_title = row[2]
        book_title = row[3]
        subject_title = row[4]
        lesson_title = row[5]
        mark_value = row[6]

        cursor.execute("SELECT * FROM students WHERE name = %s AND second_name = %s", (name, second_name))
        result_students = cursor.fetchone()
        cursor.fetchall()

        cursor.execute("SELECT * FROM books WHERE title = %s", (book_title,))
        result_books = cursor.fetchone()
        cursor.fetchall()

        cursor.execute("SELECT * FROM `groups` WHERE title = %s", (group_title,))
        result_groups = cursor.fetchone()
        cursor.fetchall()

        cursor.execute("SELECT * FROM lessons WHERE title = %s", (lesson_title,))
        result_lessons = cursor.fetchone()
        cursor.fetchall()

        cursor.execute("SELECT * FROM subjets WHERE title = %s", (subject_title,))
        result_subjects = cursor.fetchone()
        cursor.fetchall()

        cursor.execute("SELECT * FROM marks WHERE value = %s", (mark_value,))
        result_marks = cursor.fetchone()
        cursor.fetchall()

        missing_values = []

        if result_students is None:
            missing_values.extend([name, second_name])
        if result_books is None:
            missing_values.append(book_title)
        if result_groups is None:
            missing_values.append(group_title)
        if result_lessons is None:
            missing_values.append(lesson_title)
        if result_subjects is None:
            missing_values.append(subject_title)
        if result_marks is None:
            missing_values.append(mark_value)

        if missing_values:
            data.append(missing_values)

missing_values_combined = []
for item in data:
    missing_values_combined.extend(item)
print(missing_values_combined)

cursor.close()
db.close()
