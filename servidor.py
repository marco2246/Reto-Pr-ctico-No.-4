import socket 
import os
import time
import platform
import sys
host="localhost"
port=8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("servidor en espera de conexiones nuevas")
active, addr = server.accept()
enviar = str

while True:
    recibido = active.recv(1024).decode(encoding="ascii", errors="ignore")

    print("Cliente: ", recibido)

    if(recibido == "date"):
        a = time.localtime() 
        c = time.asctime(a)
        enviar=c
        active.send(enviar.encode(encoding="ascii", errors="ignore"))

    elif(recibido == "os"):
        enviar = str(platform.system() + " " + platform.release() + ", " + platform.processor())
        active.send(enviar.encode(encoding="ascii", errors="ignore"))

    elif(recibido == "ls"):
        path = "/"
        dir_list = os.listdir(path)
        enviar = str(dir_list)
        active.send(enviar.encode(encoding="ascii", errors="ignore"))

active.close()