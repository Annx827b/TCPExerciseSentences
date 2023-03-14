from socket import *
import threading

def handle_client(connection_socket, address):
    print(address)
    sentence = connection_socket.recv(1024).decode()
    print(sentence)
    capitalized_sentence = sentence.upper()
    lower_sentence = sentence.lower()
    strip_sentence = sentence.strip()
    connection_socket.send(capitalized_sentence.encode())
    connection_socket.send(lower_sentence.encode())
    connection_socket.send(strip_sentence.encode())
    connection_socket.close()


serverPort = 12
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == "close\r\n":
            connectionSocket.send("Connection is closing down now :-)".encode())
            connectionSocket.close()
            break

        elif sentence.startswith("upper"):
            capitalizedSentence = sentence[6:].upper()
            connectionSocket.send(capitalizedSentence.encode())
            print(sentence)

        elif sentence.startswith("lower"):
            lowerSentence = sentence[6:].lower()
            connectionSocket.send(lowerSentence.encode())
            print(sentence)

        elif sentence.startswith("strip"):
            stripSentence = sentence[6:].strip()
            connectionSocket.send(stripSentence.encode())
            print(sentence)
    break