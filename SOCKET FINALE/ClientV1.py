from socket import *

############ SOCKET ##############

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

        elif message == "2":

            print("\n\nrecus une couleur")
            message = ""
            message = client.recv(2048)
            message = message.decode("utf8")
            print(message)

############ MAIN ###############
client = Client
clients = client.connectSocket()
while __name__ == "__main__":

    client.getMessage(clients)