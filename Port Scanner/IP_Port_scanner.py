#python34
import socket
from datetime import datetime
import sys
from threading import Thread
import time


remote_IP = input("Enter remote host to scan:")
remoteServer_IP = socket.gethostbyname(remote_IP)

def main():  
    print("-"*60)
    print("\n")
    print("Please wait...host is scanning: "+str(remoteServer_IP))
    print("-"*60)


def port_scanning(remote_IP):
    try:
        time1 = datetime.now()
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_IP, port))
            if result == 0:
                print("Port {}\t\tOpen".format(port))
            socket.close()
        time2 = datetime.now()
        print("Elapsed time: "+str(time2-time1))
    except KeyboardInterrupt:
        print("Pressed CTRL+C")
        sys.exit()
        
    except socket.gaierror as e:
        print("Bad url format url(www.example.com")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server!")
        sys.exit()


if __name__ == "__main__":
    main()
