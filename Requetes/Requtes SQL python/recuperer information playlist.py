import sqlite3

con = sqlite3.connect('sqlite.db')

cursor = con.cursor()
command = """SELECT algorithme.id_playlist,algorithme.begin_month,algorithme.end_month,algorithme.begin_time,algorithme.end_time FROM algorithme JOIN playlist
ON algorithme.id_playlist = playlist.id 
ORDER BY playlist.id """

cursor.execute(command)
result = cursor.fetchall()
print(result)