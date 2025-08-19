import socket

def start_client(server_ip="127.0.0.1", port=5555):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())
        if msg.lower() == "exit":
            break
        response = client_socket.recv(1024).decode()
        print("Server:", response)

    client_socket.close()

# Run client
start_client()
