from socket import * 

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:

	try:
		connectionSocket, clientAddr = serverSocket.accept()
		print(f"Connected with {clientAddr}")

		sentence = connectionSocket.recv(1024).decode()
		print(f"Received: {sentence}")

		capitalizedSentence = sentence.upper()
		connectionSocket.send(capitalizedSentence.encode())
		print(f"Response: {capitalizedSentence}")

		connectionSocket.close()

	except KeyboardInterrupt:
		print("\nServer Shutting!")
		break
	except Exception as e:
		print(f"Error: {e}")

serverSocket.close()
