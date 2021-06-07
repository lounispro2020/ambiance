import sqlite3
con = sqlite3.connect('sqlite.db')


cursor = con.cursor()
command = "SELECT playlist.name,algorithme.id_playlist, algorithme.begin_time, algorithme.end_time, algorithme.begin_month, algorithme.end_month FROM algorithme,playlist WHERE playlist.id = algorithme.id_playlist "
cursor.execute(command)
result = cursor.fetchall()
for pl in result:
	print("Nom | Id | H debut | H fin | mois deb | mois fin")
	print(str(pl[0])+"\t"+str(pl[1])+"\t\t"+str(pl[2])+"\t\t"+str(pl[3]) +"\t\t  "+str(pl[4])+"\t\t  "+str(pl[5]))

listeAlg = [(4,16,20,9,12),(5,12,16,9,12)]
listePl = [("test4",4),("test5",5)]
for algo in listeAlg:
	cursor = con.cursor()
	command = """INSERT INTO algorithme(id_playlist,begin_time,end_time,begin_month,end_month)
VALUES """ +str(algo)
	print(command)
	cursor.execute(command)


for playlist in listePl:
	cursor = con.cursor()
	command = """INSERT INTO playlist(name,id)
VALUES """ +str(playlist)
	cursor.execute(command)


cursor = con.cursor()
command = "SELECT playlist.name,algorithme.id_playlist, algorithme.begin_time, algorithme.end_time, algorithme.begin_month, algorithme.end_month FROM algorithme,playlist WHERE playlist.id = algorithme.id_playlist "
cursor.execute(command)
result = cursor.fetchall()
for pl in result:
	print("Nom | Id | H debut | H fin | mois deb | mois fin")
	print(str(pl[0])+"\t"+str(pl[1])+"\t\t"+str(pl[2])+"\t\t"+str(pl[3]) +"\t\t  "+str(pl[4])+"\t\t  "+str(pl[5]))
