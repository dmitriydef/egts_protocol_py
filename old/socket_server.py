import socket


def server_program():
    host = socket.gethostname()
    port = 1144

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()

    print("Connection from " + str(address))
    print("data " + str(conn.recv(5024)))
    while True:
        data = conn.recv(5024)
        if not data:
            break

        print("from connected user: " + str(data))


if __name__ == '__main__':
    server_program()
