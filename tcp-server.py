import socket
import threading

IP = '127.0.0.1'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP, PORT))

    server.listen(5)

    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()

        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket:
        request = client_socket.recv(1024)
        print(f'[*] received: {request.decode("utf-8")}')
        client_socket.send(b'hi du')

if __name__ == "__main__":
    main()
