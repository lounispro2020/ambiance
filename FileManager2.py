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



length = len(os.listdir('C:/Users/trf_i/OneDrive/Bureau/server/Playlist/'))

def run() :
     while length > 0: 
        playsound ("C:/Users/trf_i/OneDrive/Bureau/server/Playlist/musique.mp3")


music = multiprocessing.Process(target=run)



global premierefois

premierefois=True


if __name__ == '__main__':

        while True:
        
                question = input("received y/n: ")
                if input :
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

                        
                
                







