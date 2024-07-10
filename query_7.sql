SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';


SELECT s.id AS student_id, s.fullname, gr.grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
WHERE s.group_id = 1 AND gr.subject_id = 2;

