import sqlite3
con = sqlite3.connect('sqlite.db')


cursor = con.cursor()
command = "SELECT algorithme.id_led,led_color.color, algorithme.min_temp, algorithme.max_temp FROM algorithme,led_color WHERE led_color.id = algorithme.id_led "
cursor.execute(command)
result = cursor.fetchall()
print(result)