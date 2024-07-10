SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

SELECT sub.id, sub.name
FROM grades gr
JOIN subjects sub ON gr.subject_id = sub.id
WHERE gr.student_id = 15 AND sub.teacher_id = 2;
