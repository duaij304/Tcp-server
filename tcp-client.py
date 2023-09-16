import socket

target_host = "127.0.0.1"  
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
    client.connect((target_host, target_port))
    print(f"[*] Connected to {target_host}:{target_port}")

    # Send data to the server
    client.send(b"Hello, server!")

    # Receive data from the server
    response = client.recv(1024)
    print(f"[*] Received: {response.decode()}")

except Exception as e:
    print(f"[-] Error: {str(e)}")

finally:
    client.close()
