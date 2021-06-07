import sqlite3

con = sqlite3.connect('sqlite.db')

cursor = con.cursor()

command = """SELECT playlist.id,music.path FROM music JOIN playlist
ON music.id_playlist = playlist.id
ORDER BY playlist.id"""

cursor.execute(command)
result = cursor.fetchall()
print(result)