import socket

def scan_ports(target, start_port, end_port):
    print(f"🔎 Scanning {target} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # half second timeout
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    banner = sock.recv(1024).decode().strip()
                except:
                    banner = "No banner"
                print(f"✅ Port {port} is OPEN | Banner: {banner}")
            sock.close()
        except Exception as e:
            print(f"❌ Error on port {port}: {e}")

# Example usage
scan_ports("127.0.0.1", 20, 100)
