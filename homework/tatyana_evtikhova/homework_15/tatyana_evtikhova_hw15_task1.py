import mysql.connector as mysql

db = mysql.connect(user='st-onl', passwd='AVNS_tegPDkI5BlB2lW5eASC',
                   host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
                   port=25060, database='st-onl')

cursor = db.cursor()

cursor.execute('INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)',
               ('Magic group', 'Jul 24', 'Oct 24'))

cursor.execute('INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)',
               ('Julio', 'Hernandez', cursor.lastrowid))

student_id_query = \
    'SELECT id FROM students WHERE name = %s AND second_name = %s'
cursor.execute(student_id_query, ('Julio', 'Hernandez'))
student_id = cursor.fetchone()[0]

cursor.executemany('INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)',
                   [('How not to drop database?', student_id),
                    ('What is team building?', student_id),
                    ('How to populate fields correctly', student_id)])

cursor.executemany('INSERT INTO subjets (title) VALUES (%s)',
                   [('Not for losers',), ('Pretty easy programming',
                                          ), ('What is DB?',)])

cursor.executemany('INSERT INTO lessons (title, subject_id) '
                   'SELECT %s, id FROM subjets WHERE title = %s',
                   [
                       ('1st lesson', 'Not for losers'),
                       ('2nd lesson', 'Not for losers'),
                       ('1st lesson', 'Pretty easy programming'),
                       ('2nd lesson', 'Pretty easy programming'),
                       ('1st lesson', 'What is DB?'),
                       ('2nd lesson', 'What is DB?'),
                   ])

lesson_id_query = ('SELECT id FROM lessons '
                   'WHERE title = %s AND subject_id IN (SELECT id FROM subjets WHERE title = %s)')
cursor.execute(lesson_id_query, ('1st lesson', 'Not for losers'))
lesson_id = cursor.fetchone()[0]

cursor.executemany('INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)',
                   [
                       ('Great!', lesson_id, student_id),
                       ('Good', lesson_id, student_id),
                       ('Not Good', lesson_id, student_id),
                       ('Bad', lesson_id, student_id),
                       ('Terrible', lesson_id, student_id),
                       ('Ok', lesson_id, student_id),
                   ])

for query in ['SELECT * FROM marks WHERE student_id = %s',
              'SELECT * FROM books WHERE taken_by_student_id = %s',
              '''
    SELECT s.*, b.title AS book_title, m.*, l.*, su.title AS subject_title, g.title AS group_title
    FROM students s
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjets su ON l.subject_id = su.id
    LEFT JOIN `groups` g ON s.group_id = g.id
    WHERE s.id = %s
    '''
              ]:
    cursor.execute(query, (student_id,))
    result = cursor.fetchall()
    print(result)

db.commit()
db.close()
