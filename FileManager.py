import os
import shutil
import pygame
from pygame import mixer_music as ms
from playsound import playsound
import time
from pathlib import Path
import threading 

#file_name = Path("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique_temp.txt")


length = len(os.listdir('C:/Users/trf_i/OneDrive/Bureau/server/Playlist/'))


#def rename():
#   os.rename("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique_temp.mp3", "C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3")

#if file_name.exists():
#    print("exists") 

class Music (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) :
        while length > 0: 
            playsound ("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3")



th2 = Music()

th2.start()

th2.join()             






