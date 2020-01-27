import sys,os,socket,select
adresse_hote = ''
numero_port = 8085

ma_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
ma_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ma_socket.bind((adresse_hote, numero_port))
ma_socket.listen(socket.SOMAXCONN)
surveillance = [ma_socket]

while 1:
    (event_entree, event_sortie, event_exception) = select.select(surveillance, [], [])
    for un_evenement in event_entree:
        if (un_evenement == ma_socket):
            (nouvelle_connexion, depuis) = ma_socket.accept()
            print "Nouvelle connexion depuis", depuis
            surveillance.append(nouvelle_connexion)
            nouvelle_connexion.sendall('Bienvenue\n')
            continue
        ligne = un_evenement.recv(1000)
        if not ligne:
            surveillance.remove(un_evenement)
            continue
        for desc in surveillance:
            if (desc != ma_socket) and (desc != un_evenement):
                desc.sendall(str(depuis)+": "+ ligne)
connexion.close()
ma_socket.close()
