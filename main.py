import psycopg2
from psycopg2 import DatabaseError
from faker import Faker
import random
from datetime import datetime

# Ініціалізація Faker
fake = Faker()

# Підключення до бази даних
conn = psycopg2.connect(
    database="test",
    user="postgres",
     password="s4v0e1t6a",
)
cursor = conn.cursor()

# Генерація даних для таблиць
def generate_data():
    # Додавання груп
   
    for _ in range(3):
        cursor.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))
    
    # Додавання викладачів
    for _ in range(3):
        cursor.execute("INSERT INTO teachers (fullname) VALUES (%s)", (fake.name(),))

    # Додавання предметів
    for teacher_id in range(1,4):
        for _ in range(2):
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (fake.word(), teacher_id))

    # Додавання студентів

    for group_id in range(1,4):
        for _ in range(10):
            student_id = \
            cursor.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s) RETURNING id", (fake.name(), group_id))
            student_id = cursor.fetchone()[0]
            for subject_id in range(1,7):
                cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s)", 
                           (student_id, subject_id, random.randint(0,100), fake.date_this_decade()))
    
    
    try:
        conn.commit()
    except DatabaseError  as e:
        logging.error(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()







if __name__=="__main__":
    generate_data()
 