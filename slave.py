import socket
import time
HOST = '192.168.0.19'  # The server's hostname or IP address
PORT = 65433        # The port used by the server

t1 = ""
t2 = ""
t3 = ""
t4 = ""

err = 0
final = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'BEGIN_CONNECTION')
    data = s.recv(1024)
    print('Received ', repr(data))
    t2 = time.time()
    data = s.recv(1024)
    print("Received", repr(data))
    t1 = data.decode("utf-8").split(":")[1]
    delay_req = 'DELAY_REQ:' + str(t3)
    s.sendall(bytes(delay_req, "utf-8"))            
    #t3 = time.time() - err 
    print("Sending DELAY_REQ")
    data = s.recv(1024)
    print('Received ', repr(data))
