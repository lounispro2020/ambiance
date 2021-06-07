import sqlite3
con = sqlite3.connect('sqlite.db')


cursor = con.cursor()
command = "SELECT led_color.color ,algorithme.id_led, algorithme.min_temp, algorithme.max_temp FROM algorithme,led_color WHERE led_color.id = algorithme.id_led "
cursor.execute(command)
result = cursor.fetchall()
print(result)
listeLed = [("126,126,0",4),("0,126,126",5)]
listeAlgo = [(4,6,12),(5,12,18)]

for led in listeLed:
	cursor = con.cursor()
	command = """INSERT INTO led_color(color,id)
VALUES """+str(led)
	cursor.execute(command)
for algo in listeAlgo:
	cursor = con.cursor()
	command = """INSERT INTO algorithme(id_led,min_temp,max_temp)
VALUES """+str(algo)
	cursor.execute(command)

cursor = con.cursor()
command = "SELECT led_color.color ,algorithme.id_led, algorithme.min_temp, algorithme.max_temp FROM algorithme,led_color WHERE led_color.id = algorithme.id_led "
cursor.execute(command)
result = cursor.fetchall()
print(result)