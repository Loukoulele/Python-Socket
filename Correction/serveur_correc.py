import sys,os,socket
adresse_hote = ''
numero_port = 8085
ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
ma_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ma_socket.bind((adresse_hote, numero_port))
ma_socket.listen(socket.SOMAXCONN)
while 1:
    (nouvelle_connexion, depuis) = ma_socket.accept()
    print "Nouvelle connexion depuis ",depuis
    nouvelle_connexion.sendall('Bienvenue sur le serveur 8085 :)')
    pid = os.fork()
    if (pid) :
        pid2 = os.fork()
        if (pid2):
            while 1:
                ligne = nouvelle_connexion.recv(1000)
                print ligne
                if not ligne: break
        else:
            while 1:
                clavier = raw_input(':>')
                if not clavier: break
                nouvelle_connexion.sendall(clavier)
ma_socket.close()
