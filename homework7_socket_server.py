import asyncio
import socket
from time import sleep

CLIENTS_ANSWERS = {}
HOST = '127.0.0.1'
PORT = 55555
ALPH = 'abcdefghijklmnopqrstuvwxyz'


async def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        s.setblocking(False)
        _live = True
        start_work = 1

        while _live:
            await get_new_conn(s)

            if len(CLIENTS_ANSWERS) == 0:
                if not start_work:

                    _live = False
            else:
                start_work = 0


async def get_new_conn(s):
    await asyncio.sleep(1)

    try:
        conn, addr = s.accept()
        conn.setblocking(False)
        conn.send(bytes(
            'Welcome. I will check your knowledge alphabet. We will write one character one by one. You start.', 'utf-8'))
        print(CLIENTS_ANSWERS)
        print('from server. Accept by ', conn, addr)
        task = asyncio.create_task(clients_conversation(conn, addr))

    except:
        pass
    await asyncio.sleep(1)


async def clients_conversation(conn, addr):
    _live = True
    letters_index = 0
    with conn:
        while _live:
            try:
                data = conn.recv(1024)

                if data.strip() == bytes(ALPH[letters_index], 'utf-8'):
                    letters_index += 2
                    if letters_index == 26:

                        conn.send(
                            bytes("Last letter - z. Good job. Take a pie from the shelf.", 'utf-8'))
                        _live = False
                        del CLIENTS_ANSWERS[addr]
                    else:

                        conn.send(bytes(ALPH[letters_index-1], 'utf-8'))
                        CLIENTS_ANSWERS[addr] = letters_index
                elif data:
                    conn.send(
                        bytes(f'Wrong. Next letter must be {ALPH[letters_index]}', 'utf-8'))
                    _live = False
                    del CLIENTS_ANSWERS[addr]
                elif not data:
                    _live = False
                    del CLIENTS_ANSWERS[addr]
            except:
                pass
            await asyncio.sleep(1)


asyncio.run(echo_server(HOST, PORT))

print('Done!')
