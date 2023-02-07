# import socket
# import threading
# import json
# import os
#
#
# def enter_server():
#     os.system('cls||clear')
#     # Enter servers.json to print the names of the servers
#     with open('servers.json') as f:
#         data = json.load(f)
#     print('Your servers: ', end="")
#     # Print the servers that are stored in the servers.json file
#     for servers in data:
#         print(servers, end=" ")
#     # Ask user for the name of the server to join
#     server_name = input("\nEnter the server name:")
#     global nickname
#     global password
#     nickname = input("Choose Your Nickname:")
#     if nickname == 'admin':
#         password = input("Enter Password for Admin:")
#
#     # Store the ip and port number for connection
#     ip = data[server_name]["ip"]
#     port = data[server_name]["port"]
#     global client
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # Connect to a host
#     client.connect((ip, port))
#
#
# def add_server():
#     os.system('cls||clear')
#     server_name = input("Enter a name for the server:")
#     server_ip = input("Enter the ip address of the server:")
#     server_port = int(input("Enter the port number of the server:"))
#
#     with open('servers.json', 'r') as f:
#         data = json.load(f)
#     # Store the info of the new server in servers.json
#     with open('servers.json', 'w') as f:
#         data[server_name] = {"ip": server_ip, "port": server_port}
#         json.dump(data, f, indent=4)
#
#
# # Menu loop, it will loop until the user choose to enter a server
# while True:
#     os.system('cls||clear')
#     option = input("(1)Enter server\n(2)Add server\n")
#     if option == '1':
#         enter_server()
#         break
#     elif option == '2':
#         add_server()
#
# stop_thread = False
#
#
# def recieve():
#     while True:
#         global stop_thread
#         if stop_thread:
#             break
#         try:
#             message = client.recv(1024).decode('ascii')
#             if message == 'NICK':
#                 client.send(nickname.encode('ascii'))
#                 next_message = client.recv(1024).decode('ascii')
#                 if next_message == 'PASS':
#                     client.send(password.encode('ascii'))
#                     if client.recv(1024).decode('ascii') == 'REFUSE':
#                         print("Connection is Refused !! Wrong Password")
#                         stop_thread = True
#                 # Clients those are banned can't reconnect
#                 elif next_message == 'BAN':
#                     print('Connection Refused due to Ban')
#                     client.close()
#                     stop_thread = True
#             else:
#                 print(message)
#         except:
#             print('Error Occured while Connecting')
#             client.close()
#             break
#
#
# def write():
#     while True:
#         if stop_thread:
#             break
#         # Getting Messages
#         message = f'{nickname}: {input("")}'
#         if message[len(nickname) + 2:].startswith('/'):
#             if nickname == 'admin':
#                 if message[len(nickname) + 2:].startswith('/kick'):
#                     # 2 for : and whitespace and 6 for /KICK_
#                     client.send(f'KICK {message[len(nickname) + 2 + 6:]}'.encode('ascii'))
#                 elif message[len(nickname) + 2:].startswith('/ban'):
#                     # 2 for : and whitespace and 5 for /BAN
#                     client.send(f'BAN {message[len(nickname) + 2 + 5:]}'.encode('ascii'))
#             else:
#                 print("Commands can be executed by Admins only !!")
#         else:
#             client.send(message.encode('ascii'))
#
#
# recieve_thread = threading.Thread(target=recieve)
# recieve_thread.start()
# write_thread = threading.Thread(target=write)
# write_thread.start()
#

import socket

auth = b'\x01\x00\x00\x0b\x00(\x00\x01\x00\x01\xa5\x19\x00:\t\x85\x00\x00\x00\x00\xc7\x97\x9f\x18\x01\x01\x01\x16\x00' \
       b'\x00\x00\x00\x00\x03\x00\x008687280351376597\xcc'

test = '0100010B0069005BF301435E005CF301FBA1264F02021018006470A2187847297C049BEB3D810000440000000010B80100110400080C0000180400010000001203000000001018008570A2187847297C049BEB3D810000440000000010B80100110400080C000018040001000000120300000000C01E'

test2 = '0100030B001300860001B608005F0099020000000101010500B0090200100DCE'

sock = socket.socket()
sock.connect(('localhost', 1144))
sock.send(bytes.fromhex(test2))

data = sock.recv(1024)
sock.close()

print(data.hex())