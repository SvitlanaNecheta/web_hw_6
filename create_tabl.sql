
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id SERIAL PRIMARY key,
    name VARCHAR(150) NOT NULL
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id SERIAL PRIMARY key,
    fullname VARCHAR(50) NOT NULL,
    group_id INTEGER REFERENCES groups(id) on delete cascade
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id SERIAL PRIMARY key,
    fullname VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id SERIAL PRIMARY key,
    name VARCHAR(180) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id) on delete cascade
);

DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id SERIAL PRIMARY key,
    student_id INTEGER REFERENCES students(id) on delete cascade,
    subject_id INTEGER REFERENCES subjects(id) on delete cascade,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    date_received DATE NOT NULL
);