import socket

def start_server(host="127.0.0.1", port=5555):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"🚀 Server started on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"✅ Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("❌ Connection closed")
            break
        print(f"📩 Received: {data}")
        conn.send(f"Echo: {data}".encode())

    conn.close()
    server_socket.close()

# Run server
start_server()
