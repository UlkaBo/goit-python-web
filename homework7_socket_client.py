import socket
import threading
from time import sleep


def simple_client(host, port):

    _live = True

    with socket.socket() as s:
        s.connect((host, port))
        data = s.recv(1024)
        print(f'server: {data.decode("utf-8")}')
        while _live:
            try:
                s.sendall(bytes(input(">>> "), 'utf-8'))
                data = s.recv(1024)
                print(f'server: {data.decode("utf-8")}')
                if data.decode('utf-8')[:5].lower() == 'wrong':
                    _live = False
                if data.decode('utf-8')[:4].lower() == 'last':
                    _live = False
            except ConnectionRefusedError:
                sleep(0.5)


HOST = '127.0.0.1'
PORT = 55555

simple_client(HOST, PORT)

print('done client')
