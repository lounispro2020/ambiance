import os
import shutil
import pygame
from pygame import mixer_music as ms
from playsound import playsound
import time
from pathlib import Path
import multiprocessing
from multiprocessing import Process
import threading

from socket import *

class Client:

############# SOCKET ###############
    def connectSocket():

        client = socket(AF_INET, SOCK_STREAM)
        print("try to connect...")
        connected = False
        while not connected:
            try:
                client.connect(("localhost",5699))
                connected = True
                print("...connected")
            except Exception as e:
                pass
        

        return client


    def getMessage(client):
        message = ""
        message = client.recv(1024)
        message = message.decode("utf8")
        print(message)

        if message == "1":
            return(True)

        elif message == "2":
            return(False)
            
    def musique(client):
        print("\n\nrecus une musique")
        size = client.recv(2048)
        size = size.decode("utf8")
        total = 0
        music_chunk = client.recv(2048) # 2048 bytes 
        total = total + 2048
           
        file = open('test.mp3',"wb")
        file.write(music_chunk)
        print("downloading...")
               
        while music_chunk:
                
            if total < int(size):
                file.write(music_chunk)
                music_chunk = client.recv(2048)
                total = total + 2048
            else:   
                music_chunk = False
                total = 0

        print("File was succesfully download !")
        file.close()
        return True

    def led(client):
        print("\n\nrecus une couleur")
        message = ""
        message = client.recv(2048)
        message = message.decode("utf8")
        print(message)
        return(message)



############ MAIN ###############
client = Client
clients = client.connectSocket()


length = len(os.listdir('C:/Users/trf_i/OneDrive/Bureau/server/Playlist/'))

def run() :
     while length > 0: 
        playsound ("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3")


music = multiprocessing.Process(target=run)



global premierefois

premierefois=True


if __name__ == '__main__':

    while True:
        message = client.getMessage(clients)
        if message:
            musique = client.musique(clients)
        elif !message:
            led = client.led(clients)

        if musique:

            if(premierefois):
                premierefois=False
                os.rename('C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique_temp.mp3','C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3') 
                music.start()
            else:
                print("Is thread1 alive:", music.is_alive())
                music.terminate()
                music.join()
                os.remove("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3")
                os.rename('C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique_temp.mp3','C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3')
                music = multiprocessing.Process(target=run)
                music.start()
