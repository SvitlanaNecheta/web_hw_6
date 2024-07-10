SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT AVG(gr.grade) as average_grade
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE sub.teacher_id = 2;

