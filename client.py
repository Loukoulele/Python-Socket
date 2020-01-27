import os, socket, sys, atexit

adresse_serveur = socket.gethostbyname('localhost')
numero_port = 8085
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    my_socket.connect((adresse_serveur, numero_port))
except Exception:
    print("Probleme de connexion")
    sys.exit(1)
while 1:
    while 1:
        msg = input()
        my_socket.send(msg.encode('utf-8'))
        break
    while 1:
        msg = my_socket.recv(1024)
        print(msg.decode('utf-8'))

my_socket.close()
