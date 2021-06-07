import sqlite3
con = sqlite3.connect('sqlite.db')


cursor = con.cursor()
command = "SELECT * FROM music"
cursor.execute(command)
result = cursor.fetchall()
print(result)



liste = [(11,'musique 11',1,'musique 11.mp3','.mp3',"test"),(12,'musique 12',2,'musique 12.mp3','.mp3',"test"),(13,'musique 13',3,'musique 13.mp3','.mp3',"test"),(14,'musique 14',2,'musique 14.mp3','.mp3',"test"),(15,'musique 15',1,'musique 15.mp3','.mp3',"test")]

i = 0
for music in liste:
    cursor = con.cursor()
   
    command = """INSERT INTO music(id,name,id_playlist,path,format,artist)
VALUES """ + str(music)
    cursor.execute(command)
    result = cursor.fetchall()



cursor = con.cursor()
command = "SELECT * FROM music"
cursor.execute(command)
result = cursor.fetchall()
print(result)