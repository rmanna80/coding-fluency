
import socket

with socket.create_connection(("127.0.0.1", 9001), timeout=5) as s:
    s.sendall(b"Hello from Python!\n")
    print("Test message sent.")
