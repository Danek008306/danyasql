import sqlite3
from sqlite3 import Cursor

conn = sqlite3.connect('student.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade REAL
)
''')

cursor.execute('''
INSERT INTO students (name, grade)
VALUES ('Masha',175.5),('Danya',188), ('Vanya',170.5)
''')

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
