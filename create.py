import logging
from psycopg2 import DatabaseError
from connect import create_conection

def create_table(conn,sql_expression:str): 
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """ 
    c = conn.cursor()
    try:
       
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError  as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_drop_create_groups_table = """
    DROP TABLE IF EXISTS groups CASCADE;
    CREATE TABLE groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );
    """
    
    sql_drop_create_students_table = """
    DROP TABLE IF EXISTS students CASCADE;
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(50) NOT NULL,
        group_id INTEGER REFERENCES groups(id) ON DELETE CASCADE
    );
    """
    
    sql_drop_create_teachers_table = """
    DROP TABLE IF EXISTS teachers CASCADE;
    CREATE TABLE teachers (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(50) NOT NULL
    );
    """
    
    sql_drop_create_subjects_table = """
    DROP TABLE IF EXISTS subjects CASCADE;
    CREATE TABLE subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(180) NOT NULL,
        teacher_id INTEGER REFERENCES teachers(id) ON DELETE CASCADE
    );
    """
    
    sql_drop_create_grades_table = """
    DROP TABLE IF EXISTS grades CASCADE;
    CREATE TABLE grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
        subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
        grade INTEGER CHECK (grade >= 0 AND grade <= 100),
        date_received DATE NOT NULL
    );
    """

    try:
        with create_conection() as conn:
            if conn is not None:
                # create all tables
                create_table(conn, sql_drop_create_groups_table)
                create_table(conn, sql_drop_create_students_table)
                create_table(conn, sql_drop_create_teachers_table)
                create_table(conn, sql_drop_create_subjects_table)
                create_table(conn, sql_drop_create_grades_table)
            else:
                logging.error("Error! Cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)