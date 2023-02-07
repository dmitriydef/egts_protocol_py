import socket

from egts import egts

s = socket.socket()
s.bind(('', 1144))
s.listen(1)

conn, addr = s.accept()

pid = 0
rid = 0

with conn:
    data = conn.recv(1024)
    if not data:
        print('ERROR. server has closed the connection. No packets were received.')
        s.close()

    response = egts.Egts(data)
    print(response.service)
    reply = response.reply(pid, rid)
    conn.send(reply)
    pid += 1
    rid += 1

# from egts import egts
#
# test = '0100030B001300860001B608005F0099020000000101010500B0090200100DCE'
#
# buff = bytes.fromhex(test)
#
# res = egts.Egts(buffer=buff)
#
# reply = res.reply(1, 1)
#
# print(reply.hex())
# #
# # tl = transport_layer.TransportLayer(buff)
# # sl = service_layer.ServiceLayer(buff[tl.header_length:])
# # sl.print_service_layer()
# #
# # # tl.print_transport_layer()
# # print(int.from_bytes(b'\xB6', byteorder='little'))
