import psycopg2
conn = psycopg2.connect(database="Employee",
                        host="localhost",
                        user="postgres",
                        password="Anas907",
                        port="5432")
# Creating table
cursor = conn. cursor()

cursor=conn.cursor()
cursor.execute('select * from employee')
rows=cursor.fetchall()
print(rows)