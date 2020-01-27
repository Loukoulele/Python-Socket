import os,socket,sys

adresse_serveur = socket.gethostbyname('localhost')
numero_port = 8085
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def lecture_ligne(x, my_socket):
    ligne = x
    while 1:
        caractere_courant = my_socket.recv(1)
        if not caractere_courant:
            break
        if caractere_courant == '\r':
            caractere_suivant = my_socket.recv(1)
            if caractere_suivant == '\n':
                break
            ligne += caractere_courant + caractere_suivant
            continue
        if caractere_courant == '\n':
            break
        ligne += caractere_courant
    return ligne

try: my_socket.connect((adresse_serveur, numero_port))
except Exception, description:
    print "Probleme de connexion", description
    sys.exit(1)
while 1:
    x = raw_input() + "\n"
    ligne = lecture_ligne(x,my_socket)
    my_socket.sendall(ligne)
    # ligne = my_socket.recv(1024)
    if not ligne: break
    else:
        print ligne
my_socket.close()
