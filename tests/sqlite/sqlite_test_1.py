import sqlite3

conn = sqlite3.connect('family.db')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE family
                    (name, relationship, age, phone_number)
                ''')
                
cursor.execute("INSERT INTO family VALUES ('Zachery', 'brother', 21, 9032190742)")

conn.commit()
