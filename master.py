import socket
import time
HOST = '150.162.50.93'  # Standard loopback interface address (localhost)
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)

currState = 0


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    while True:
        with conn:
            while True:
                if currState == 0:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode('utf-8') == "BEGIN_CONNECTION":
                        timestamp = time.time()
                        conn.sendall(b'SYN')
                        str = 'FOLLOW_UP:' + str(timestamp)
                        conn.sendall(bytes(str, 'utf-8'))
                    if data.decode('utf-8') == "DELAY_REQ":
                        print('receveid delay req')
                        conn.sendall(b'DELAY_RES')

