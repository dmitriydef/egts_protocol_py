import socket

from egts import egts as egts_test

sock = socket.socket()
sock.bind(('', 1144))
sock.listen(1)

pid = 0
rid = 0

while True:
    conn, addr = sock.accept()
    print('connection on ', addr)

    while True:
        data = conn.recv(1024)

        response = egts_test.Egts(data)

        print(response)
        reply = response.reply(pid, rid)
        conn.send(reply)

        pid += 1
        rid += 1
        if not data:
            break
        conn.send(data)

    pid = 0
    rid = 0

    conn.close()
