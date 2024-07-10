SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';


SELECT  
ROUND(AVG(grade), 2) as average_grade
FROM grades
WHERE subject_id = 1
GROUP BY student_id
ORDER BY average_grade DESC
LIMIT 1;

