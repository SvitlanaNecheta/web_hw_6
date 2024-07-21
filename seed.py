from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import date
from models import Student, Group, Teacher, Subject, Grade, engine

# Ініціалізація Faker та сесії
faker = Faker()
Session = sessionmaker(bind=engine)
session = Session()

print("Trying to connect to the database...")
try:
    session.execute('SELECT 1')
    print("Connection successful.")
except Exception as e:
    print(f"Connection failed: {e}")

print("Performing database operations...")

# Створення груп
groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(fullname=faker.name()) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [Subject(name=f"Subject {i+1}", teacher=random.choice(teachers)) for i in range(6)]
session.add_all(subjects)
session.commit()

# Створення студентів
students = [Student(fullname=faker.name(), group=random.choice(groups)) for _ in range(40)]
session.add_all(students)
session.commit()

# Створення оцінок
grades = []
for student in students:
    for subject in subjects:
        for _ in range(random.randint(5, 10)):
            grades.append(Grade(
                student=student,
                subject=subject,
                grade=random.uniform(60, 100),
                date_received=faker.date_between(start_date='-2y', end_date='today')
            ))

session.add_all(grades)
session.commit()

print("Database seeded successfully!")

print("Closing the connection.")
session.close()
