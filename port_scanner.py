import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

# Example usage
target_host = input("Enter target IP or hostname: ")
common_ports = [22, 80, 443, 8080]
scan_ports(target_host, common_ports)
