SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';


SELECT g.id AS group_id, AVG(gr.grade) as average_grade
FROM grades gr
JOIN students s ON gr.student_id = s.id
JOIN groups g ON s.group_id = g.id
WHERE gr.subject_id = 1
GROUP BY g.id;

