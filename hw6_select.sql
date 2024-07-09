SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT s.id, s.fullname,
ROUND(AVG(grade), 2) as average_grade
FROM students s 
join grades g  on s.id=g.student_id 
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;

SELECT  
ROUND(AVG(grade), 2) as average_grade
FROM grades
WHERE subject_id = 1
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;

SELECT g.id AS group_id, AVG(gr.grade) as average_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
WHERE gr.subject_id = 1
GROUP BY g.id;

SELECT AVG(grade) as average_grade
FROM grades;

SELECT id, name
FROM subjects
WHERE teacher_id = 1;

SELECT id, fullname
FROM students
WHERE group_id = 2;

SELECT s.id AS student_id, s.fullname, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = 1 AND gr.subject_id = 2;

SELECT AVG(gr.grade) as average_grade
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.teacher_id = 2;

SELECT sub.id, sub.name
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE gr.student_id = 12;

SELECT sub.id, sub.name
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE gr.student_id = 15 AND sub.teacher_id = 2;
