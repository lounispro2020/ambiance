import sqlite3

con = sqlite3.connect('sqlite.db')

cursor = con.cursor()

command = "SELECT path,id_playlist FROM music"

cursor.execute(command)
result = cursor.fetchall()
print(result)