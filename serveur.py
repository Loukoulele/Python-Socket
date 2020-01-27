import os, socket, sys

numero_port = 8085
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind(('', numero_port))
my_socket.listen(socket.SOMAXCONN)
nouvelle_connexion = None

while 1:
    if not nouvelle_connexion:
        (nouvelle_connexion, TSAP_depuis) = my_socket.accept()
        nouvelle_connexion.sendall("Bienvenue sur le serveur 8085\n".encode('utf-8'))
        print("Nouvelle connexion depuis", TSAP_depuis)
        pid = os.fork()
    if (pid):
        while 1:
            msg = nouvelle_connexion.recv(1024)
            print(msg.decode('utf-8'))
            break
        while 1:
            msg = input()
            nouvelle_connexion.sendall(msg.encode('utf-8'))
            break

my_socket.close()
