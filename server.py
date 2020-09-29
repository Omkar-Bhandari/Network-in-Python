import socket
from _thread import *

server = "ip_address"
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e :
    print(str(e))

s.listen()
print("Server Initialized....\n\nWaiting FOr Connections..\n")

def readpos(str):
    str = str.split(",")
    return int(str[0]) , int(str[1])

def makepos(tup):
    return str(tup[0]) + "," +str(tup[1])

pos = [(0,0),(400,0)]

def thread_1(conn,player):

    conn.send(str.encode(makepos(pos[player])))

    reply = ""
    while True:
        try:
            data = readpos(conn.recv(2048).decode())

            pos[player] = data

            if len(data) < 1:
                print("Discoonected from ",addr)
                break
            else:

                if player == 1 :
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recieved: ",data)
                print("Sending: ",reply)

            conn.sendall(str.encode(makepos(reply)))

        except:
            print("Error")
            break


    print("Disconnected..\nWaiting FOr New Connection..")
    conn.close()

currentPlayer = 0
while True:
    conn , addr = s.accept()
    print(f"Connection Established with {addr}.. \nWaiting for data... ")
    start_new_thread(thread_1,(conn,currentPlayer))
    currentPlayer =+ 1
