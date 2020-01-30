import os,socket,sys
adresse_serveur = 'localhost'
numero_port = 8085
ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = os.popen('whoami').read()
try:
    ma_socket.connect((adresse_serveur, numero_port))
    # ma_socket.sendall(name)
except:
    print "probleme de connexion"
    sys.exit(1)
pid = os.fork()
if (pid) :
    while 1:
        ligne = ma_socket.recv(1000)
        print ligne
        if not ligne: break
else:
    while 1:
        clavier = raw_input(':>')
        if not clavier: break
        ma_socket.sendall(clavier)
ma_socket.close()
