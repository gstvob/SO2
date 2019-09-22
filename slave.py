import socket
import time
HOST ='192.168.0.19'  # The server's hostname or IP address
PORT = 65434        # The port used by the server

t1 = ""
t2 = ""
t3 = ""
t4 = ""


#print(time.get_clock_info('time').implementation)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'BEGIN_CONNECTION')
    
    #SYN
    data = s.recv(1024)
    print('Received ', repr(data))
    t2 = time.time()
    print("Storing T2:" +str(t2))
    #FOLLOW UP
    data = s.recv(1024)
    print("Received", repr(data))
    t1 = data.decode("utf-8").split(":")[1]
    print("STORING T1")
    print("STORED: T1=%s, T2=%s" %(t1, str(t2)))
    #SEND DELAY REQUEST
    
    delay_req = 'DELAY_REQ:' + str(t3)
    s.sendall(bytes(delay_req, "utf-8"))            
    t3 = time.time() 
    print("Sending DELAY_REQ, storing T3:" +str(t3))
    print("STORED: T1=%s, T2=%s, T3=%s" %(t1, str(t2), str(t3)))

    #RECEIVE DELAY
    data = s.recv(1024)
    print('Received ', repr(data))
    t4 = data.decode("utf-8").split(":")[1]
    print("ALL TIMES: T1=%s, T2=%s, T3=%s, T4=%s" %(t1, str(t2), str(t3), t4))
    propagation_delay = ((t2 - float(t1)) + (float(t4) - t3)) / 2
    offset = (t2 - float(t1)) - propagation_delay
    print("PROPAGATION DELAY: "+str(propagation_delay))
    print("OFFSET: "+str(offset))

    print("TEST")
    test_time = t2 - offset
    print("T1 = %s, T2 = %s" % (t1, str(t2)))
    print(time.ctime(float(t1)))
    print(time.ctime(t2))
