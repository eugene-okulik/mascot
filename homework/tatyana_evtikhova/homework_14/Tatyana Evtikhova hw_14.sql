INSERT INTO `groups` (title, start_date, end_date) VALUES ('Pythonic world', 'January 24', 'April 24')

INSERT INTO students (name, second_name, group_id) VALUES ('Mascot', 'Colour', 273)
INSERT INTO books (title, taken_by_student_id) VALUES ('How not to drop database?', (SELECT id FROM students WHERE id = 322))

INSERT INTO books (title, taken_by_student_id) VALUES ('Studying python while sleeping',(SELECT id FROM students WHERE id = 322)), 
('Creating best CV in 2024', (SELECT id FROM students WHERE id = 322))

INSERT INTO subjets (title) VALUES ('Best practices'), 
('Business English'), 
('Korean language for additional opportunities')

INSERT INTO lessons (title, subject_id) 
VALUES 
  ('First lesson', (SELECT id FROM subjets WHERE id = 417)), 
  ('Second lesson', (SELECT id FROM subjets WHERE id = 417))

INSERT INTO lessons (title, subject_id) 
SELECT 'First lesson', id FROM subjets WHERE id = 418
UNION ALL
SELECT 'Second lesson', id FROM subjets WHERE id = 418
UNION ALL
SELECT 'First lesson', id FROM subjets WHERE id = 419
UNION ALL
SELECT 'Second lesson', id FROM subjets WHERE id = 419

INSERT INTO marks (value, lesson_id, student_id)
SELECT 'Could be better', l.id, s.id
FROM lessons l, students s
WHERE l.id = 373 AND s.id = 322
UNION ALL 
SELECT 'Good enough', l.id, s.id 
FROM lessons l, students s
WHERE l.id = 374 AND s.id = 322
UNION ALL 
SELECT 'What a shame', l.id, s.id 
FROM lessons l, students s
WHERE l.id = 375 AND s.id = 322
UNION ALL 
SELECT 'Nice job', l.id, s.id 
FROM lessons l, students s
WHERE l.id = 376 AND s.id = 322
UNION ALL 
SELECT 'Please change', l.id, s.id 
FROM lessons l, students s
WHERE l.id = 377 AND s.id = 322
UNION ALL 
SELECT 'Ok', l.id, s.id 
FROM lessons l, students s
WHERE l.id = 378 AND s.id = 322


SELECT * FROM marks WHERE student_id = 322
SELECT * FROM books WHERE taken_by_student_id = 322
    
SELECT 
    s.*,
    b.title AS book_title,
    m.*,
    l.*,
    su.title AS subject_title,
    g.title AS group_title
FROM 
    students s
LEFT JOIN 
    books b ON s.id = b.taken_by_student_id
LEFT JOIN 
    marks m ON s.id = m.student_id
LEFT JOIN 
    lessons l ON m.lesson_id = l.id
LEFT JOIN 
    subjets su ON l.subject_id = su.id
LEFT JOIN 
    `groups` g ON s.group_id = g.id
WHERE 
    s.id = 322




