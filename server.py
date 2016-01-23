# Server_Crypter
server/client + cryptage

""" réseau côté serveur """

from socket import *

def codage(msg):
    new_msg=""
    for i in range(len(msg)) :
        new_msg=new_msg+chr(ord(msg[i])-2)
    return new_msg

def decodage(msg):
    new_msg=""
    for i in range(len(msg)) :
        new_msg=new_msg+chr(ord(msg[i])+2)
    return new_msg

#Création dde la connexion
serveur = socket(AF_INET,SOCK_STREAM)
ip_host=gethostbyname(gethostname())
print("Ton IP:",ip_host)

#Configuration du socket pour qu'il écoute sur le port 12800
serveur.bind(('',12800))

#Faire écouter le socket, 5 connexion au maximum
serveur.listen(5)

#attente de la connexion d'un client, le programme se bloque
connexion_avec_client, infos_connexion = serveur.accept()

#envoi d'un message de bienvenue
connexion_avec_client.send(b"Serveur vient d'accepter la connexion")

while True:
    # attente d'un message
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu = decodage(msg_recu.decode())

    #décoder et afficher le message
    print(msg_recu)

    #création d'un message
    msg_a_envoyer = input("REPONDRE : ")
    msg_a_envoyer = codage(msg_a_envoyer)

    #envoi d'un message
    connexion_avec_client.send(msg_a_envoyer.encode())
    
    
