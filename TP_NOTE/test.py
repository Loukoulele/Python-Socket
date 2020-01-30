import socket
import struct
import os
import time

host = '224.0.0.127'
port = 7186

def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

name = os.popen('whoami').read()[:-1]

socket_io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_io.bind(('', port))

TSAP = (host, port)
mreq = struct.pack("4sl", socket.inet_aton(host), socket.INADDR_ANY)

socket_io.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

pid = os.fork()
i=0
check = False
fa = False
if pid:
    while True:
        (data, (ip, port)) = socket_io.recvfrom(1000)
        out = data.decode('utf-8')
        pseudo_split = out.split(':')
        pseu = pseudo_split[0]
        pseu = listToString(pseu)
        f=open("user.txt", "a+")
        f1 = f.readlines()
        with open("user.txt", "r") as fx:
            for line in fx.readlines():
                line2 = line.split(';')
                line2 = line2[1]
                line2 = line2[:-1]
                if line2 == pseu:
                    check = True
        if check == False:
            for i in range(1):
                f.write(ip+";"+pseudo_split[0]+"\r\n")
        check = False
        if out.startswith('@{}'.format(name)):
            print(out)
        elif out.startswith('@'):
            continue
        else:
            print(bcolors.OKGREEN + out + bcolors.ENDC)
else:
    while True:
        time.sleep(0.1)
        clavier = input(bcolors.OKBLUE + '@:>' + bcolors.ENDC)
        if clavier == '!':
            print(bcolors.WARNING + "List ------------------------------------>\n")
            f=open("user.txt", "a+")
            f1 = f.readlines()
            with open("user.txt", "r") as f:
                for line in f.readlines():
                    line = line.split(';')
                    print(bcolors.OKGREEN + line[1][:-1] + bcolors.WARNING)
            print("\n<------------------------------ End List  " + bcolors.ENDC)
        else:
            to_send = ''
            if clavier != '':
                if clavier[0] == '>':
                    x = clavier.split()
                    x2 = x[0][1:]
                    f=open("user.txt", "a+")
                    f1 = f.readlines()
                    with open("user.txt", "r") as f:
                        for line in f.readlines():
                            line = line.split(';')
                            line2 = line[1][:-1]
                            if line2 == x2:
                                to_send = line[0]
                                new_pseudo = line[1]
                    x.pop(0)
                    x = " ".join(x)
                    n_clavier = clavier.split()
                    try:
                        t = n_clavier[1]
                    except IndexError:
                        fa = True
                    if fa == True:
                        print('Message vide')
                    else:
                        new_send = name + ":" + new_pseudo[:-1]
                        if x == '':
                            x = '\n'
                        msg = "{}:{} ".format(new_send, x)
                        UNICAST_TSAP = (to_send, port)
                        socket_io.sendto(msg.encode('utf-8'), UNICAST_TSAP)
                else:
                    if clavier == '':
                        clavier = '\n'
                    msg = "{}: {}".format(name, clavier)
                    socket_io.sendto(msg.encode('utf-8'), TSAP)
                if not clavier:
                    break

socket_io.close()
