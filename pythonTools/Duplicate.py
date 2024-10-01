import serial
import time
import random
import socket

# Socket Config
ip_address = '10.0.0.2'  # Change this to the IP address of your device
port = 90

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
sock.bind((ip_address, port))

# Start listening for incoming connections
sock.listen(1)  # Listen for only one connection

print(f"Listening for connections on {ip_address}:{port}...")

# Accept incoming connection
connection, address = sock.accept()

print(f"Connection established from {address}")


def generate_data():
    """
    Generates a string of 5 numbers, each within the same order of magnitude,
    separated by commas. Adjust the ranges according to your needs.
    """
    return ','.join(str(random.randint(1, 9) * 10 ** i) for i in range(5))
