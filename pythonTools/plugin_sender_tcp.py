import socket
import time

HOST = "0.0.0.0"  # Escuchar desde cualquier IP
PORT = 5050       # El mismo que en el plugin

with open("loratestdata.txt", "r") as f:
    lines = [
        line.strip().split(" ", 3)[-1] + "\r\n"
        for line in f if "," in line
    ]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"🟢 Escuchando en {HOST}:{PORT}...")
conn, addr = server.accept()
print(f"✅ Conectado con: {addr}")

try:
    for line in lines:
        conn.sendall(line.encode('utf-8'))
        print(f"Sent: {line.strip()}")
        time.sleep(1)
except KeyboardInterrupt:
    print("⛔ Interrumpido.")
finally:
    conn.close()
    server.close()
