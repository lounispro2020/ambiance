import sqlite3
import random
from datetime import datetime
from socket import *
import time

import os


def getRandomMusic(hour, month):

    con = sqlite3.connect('sqlite.db')

    cursor = con.cursor()

    command = """ SELECT music.path FROM music JOIN playlist 
	ON music.id_playlist = playlist.id
	JOIN algorithme
	ON playlist.id = algorithme.id_playlist
	WHERE algorithme.begin_time <= """+ hour + """
	AND algorithme.end_time >=""" + hour +"""
	AND algorithme.begin_month <= """ + month + """
	AND algorithme.end_month >= """ + month

    cursor.execute(command)

    result = cursor.fetchall()
    music = ""
    rd = random.randint(0, len(result)-1)
    i = 0
    for res in result:
        if i == rd:
            music = res[0] 
        i +=1

    return(music)

def getTemp():
	con = sqlite3.connect('sqlite.db')

	cursor = con.cursor()

	command = """ SELECT temperature FROM temperature
    GROUP BY date_time
    ORDER BY date_time DESC LIMIT 1 """

	cursor.execute(command)

	result = cursor.fetchone()
	return(str(result[0]))


def getColor(temp):
	con = sqlite3.connect('sqlite.db')

	cursor = con.cursor()

	command = """SELECT led_color.color FROM led_color JOIN algorithme
	ON led_color.id = algorithme.id_led
	WHERE algorithme.max_temp >= """ + temp + """
	AND algorithme.min_temp <= """ + temp 

	cursor.execute(command)

	result = cursor.fetchone()
	return(result[0])



############ SOCKET ##############

class Server:


    def connectSocket():
        
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(("", 5699))
        server.listen(5)
        print("en ecoute...")
        #self.condition()

        print("en attente d'un client")
        client, addr = server.accept()
        print("...client connecté")

        return client

    def sendRequest(requestType):
        clients = server.connectSocket()
        requestType.encode("utf-8")
        clients.sendall(requestType)
        clients.close()
       
    def sendLed(client,files):
        Id = "2"
        Id = Id.encode("utf8")
        files = files.encode("utf8")
        client.send(Id)
        client.send(files)
        



    def sendMusic(client,files):
        Id = "1"
        Id = Id.encode("utf8")
        client.send(Id)
        size = os.path.getsize(files)

        fileSize = str(size)

        fileSize = fileSize.encode("utf8")

        print(size)
        client.send(fileSize)


        file = open(files,"rb")
        music_data = file.read(2048)

        print("envoid de des donnée de la musique...")

        while music_data:
            client.send(music_data)
            music_data = file.read(2048)

        print("La musique à ete tranferé !")

        file.close()
        
############ MAIN ###############


server = Server
client = server.connectSocket()
#while True: 
today = datetime.today()
month = str(today.month)
hour = str(today.hour)

FileMusic = getRandomMusic(hour, month)
print("musique: ")
print(FileMusic)

temperature = getTemp()
print("\ntemperature: ")
print(temperature)

color = getColor(temperature)

print("\nled color: ")
print(color)
    
server.sendLed(client,color)
time.sleep(5.0) 
server.sendMusic(client,FileMusic)
time.sleep(1.0)


    
