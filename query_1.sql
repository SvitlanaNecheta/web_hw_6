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

