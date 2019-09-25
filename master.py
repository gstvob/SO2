import socket
import time

HOST = '150.162.50.74'  # Standard loopback interface address (localhost)
PORT = 65444        # Port to listen on (non-privileged ports are > 1023)


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
            t4 = time.time()
            delay_res = 'DELAY_RES:' + str(t4)
            conn.sendall(bytes(delay_res, "utf-8"))

            data = conn.recv(2014)
            if data == b'START_TEST':
                for i in range(1000):
                    conn.sendall(bytes(str(time.time()),'utf-8'))
                    data = conn.recv(2014)
                    if data == b'SEND_NEXT':
                        continue
            #print(str(time.time()))
            #conn.sendall(bytes(str(time.time()), "utf-8"))