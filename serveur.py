import os,socket,sys

numero_port = 8085
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind(('', numero_port))
my_socket.listen(socket.SOMAXCONN)

while 1:
    (nouvelle_connexion, TSAP_depuis) = my_socket.accept()
    print "Nouvelle connexion depuis", TSAP_depuis
    nouvelle_connexion.sendall('Bienvenue\n')
    print '', nouvelle_connexion.recv(100)
    # nouvelle_connexion.close()

my_socket.close()
