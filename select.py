import logging

from psycopg2 import DatabaseError
from connect import create_conection


if __name__ == '__main__':
    sql_check_tables = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    
    sql_top_5_students = """
    SELECT s.id, s.fullname,
    ROUND(AVG(grade), 2) as average_grade
    FROM students s 
    JOIN grades g ON s.id = g.student_id 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    
    sql_best_student_subject_1 = """
    SELECT  
    ROUND(AVG(grade), 2) as average_grade
    FROM grades
    WHERE subject_id = 1
    GROUP BY student_id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    
    sql_avg_grade_group_subject_1 = """
    SELECT g.id AS group_id, AVG(gr.grade) as average_grade
    FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
    WHERE gr.subject_id = 1
    GROUP BY g.id;
    """
    
    sql_avg_grade_all = """
    SELECT AVG(grade) as average_grade
    FROM grades;
    """

    try:
        with create_conection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    # Check tables
                    c.execute(sql_check_tables)
                    tables = c.fetchall()
                    print("Tables in database:", tables)
                    
                    # Top 5 students by average grade
                    c.execute(sql_top_5_students)
                    top_students = c.fetchall()
                    print("Top 5 students by average grade:", top_students)
                    
                    # Best student in subject 1
                    c.execute(sql_best_student_subject_1)
                    best_student = c.fetchone()
                    print("Best student in subject 1:", best_student)
                    
                    # Average grade by group for subject 1
                    c.execute(sql_avg_grade_group_subject_1)
                    avg_grade_group = c.fetchall()
                    print("Average grade by group for subject 1:", avg_grade_group)
                    
                    # Average grade overall
                    c.execute(sql_avg_grade_all)
                    avg_grade_all = c.fetchone()
                    print("Average grade overall:", avg_grade_all)
                    
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                logging.error("Error! Cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)