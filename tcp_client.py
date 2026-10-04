from socket import *

serverName = '192.168.1.103'

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)

try:
	clientSocket.connect((serverName,serverPort))
	print("Connected to server")
	
	sentence = input('Input lowercase name:')
	clientSocket.send(sentence.encode())

	modifiedSentence = clientSocket.recv(1024)
	print ('From Server:', modifiedSentence.decode())


except Exception as e:
	print(f"Error: {e}")

finally:
	clientSocket.close()