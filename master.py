import socket
import time

HOST = '192.168.0.19'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)

currState = 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        if data.decode('utf-8') == "BEGIN_CONNECTION":
            t1 = time.time()
            print('Received BEGIN_CONNECTION')
            conn.sendall(b'SYN')
            print("Sending SYN")
            follow_up = 'FOLLOW_UP:' + str(t1)
            conn.sendall(bytes(follow_up, 'utf-8'))
            print("Sending FOLLOW_UP with t1 = " + str(t1))
            data = conn.recv(1024)
            print('received delay req')
            conn.sendall(b'DELAY_RES')

