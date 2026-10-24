import platform
import socket

print(f"System: {platform.system()}\nPython Version: {platform.python_version()}\nArchitecture: {platform.architecture()}\nProcessor: {platform.processor()}\n")
print("="*70)



hostname = socket.gethostname()
ip = socket.gethostbyname(hostname) 
print(f"Hostname: {hostname}\nIP: {ip}\n")
HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    """ socket.socket() creates a socket object that suppoprts the content manage type so you can use it in a with statement 
        arguments are passed to socket()
        AF_INET is the internet address for IPv4
        SOCK_STREAM is the socket type for TCP 
    """
    s.bind((HOST, PORT)) # used to associate the socety with a specific network interface and port number
    """ the IP address 127.0.0.1 is the standard IPv4 address for the loopback interface
        so only processes on that host will be able to connect to the server 
        if you pass an empty string (also host can be (passed) hostname)  the server will accept communications on all available IPv4 interfaces
        
        port represents the TCP port number to accept connnection on from clients """
    s.listen() #enables a server to accept connections 
                # if your server receives a lot of connection set a limit 
    conn, addr = s.accept() # blocks execution an dwaits for incoming connection
                            # when a new client connects it returns  a new socket object representing the connection and a tuple 
                            # holding the address of the client
    with conn:
        print(f"COnnected by {addr}")
        while True:
            data = conn.recv(1042)
            if not data:
                break
        conn.sendall(data)

"""----------------- ECHO CLIENT --------------"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1042)
print(f"Received {data!r}")




print("="*70)
print(
    "HACKBOT V1.0\n This is your friendly hackbot"
)

# ask_user = input("Enter a command: ").strip().lower()
print("\nPress Ctrl+C to exit\n")
# print(ask_user)

commands = [
    "help",
    "status",
    "diagnostics"
]

try:
    while True:
        ask_user = input("Enter a command: ").strip().lower()
        if ask_user == "help":
            print("This is help")
        elif ask_user == "status":
            print("This is status")
        print(f"You entered: {ask_user}")
except KeyboardInterrupt:
    print("\nStopped commands")