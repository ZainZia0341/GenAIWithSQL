import sqlite3

connection = sqlite3.connect("student.db")  ## if db does not exits it will be created

cursor = connection.cursor()


table_info = """
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), Section VARCHAR(1))
"""

cursor.execute(table_info)

cursor.execute("""Insert into STUDENT values('Zain', 'Data Science', 'A')""")
cursor.execute("""Insert into STUDENT values('Hasnain', 'FrontEnd', 'B')""")
cursor.execute("""Insert into STUDENT values('Mughees', 'BackEnd', 'C')""")
cursor.execute("""Insert into STUDENT values('Moheed', 'Data Science', 'D')""")

print("The inserted record are") 
data = cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

connection.commit()
connection.close()