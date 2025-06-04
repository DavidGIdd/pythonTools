import serial
import socket
import time

# === CONFIGURATION ===
SERIAL_PORT = "COM4"       # Change to your LoRa serial port
BAUD_RATE = 9600
TCP_HOST = "0.0.0.0"        # Listen on all interfaces
TCP_PORT = 5050             # Port expected by the plugin
LOG_FILE = "lora_log.txt"

# === INIT SERIAL ===
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"🟢 Serial listening on {SERIAL_PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    print(f"❌ Error opening serial port: {e}")
    exit()

# === INIT TCP SERVER ===
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_HOST, TCP_PORT))
server.listen(1)
print(f"🟢 Waiting for TCP connection on {TCP_HOST}:{TCP_PORT}...")

conn, addr = server.accept()
print(f"✅ TCP client connected from: {addr}")

# === START RELAY LOOP ===
try:
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        while True:
            if ser.in_waiting:
                raw_data = ser.readline()
                decoded = raw_data.decode(errors="ignore").strip().strip('\x00').strip('\xe1')

                if decoded:
                    message = decoded + "\r\n"
                    try:
                        conn.sendall(message.encode('utf-8'))
                        print(f"📤 Sent to TCP: {decoded}")
                    except Exception as e:
                        print(f"⚠️ Error sending to TCP: {e}")
                        break  # Break out to allow reconnect

                    # Log it
                    log_file.write(decoded + "\n")
                    log_file.flush()

            time.sleep(0.05)

except KeyboardInterrupt:
    print("\n⛔ Stopped by user.")
except Exception as e:
    print(f"💥 Unexpected error: {e}")
finally:
    conn.close()
    server.close()
    ser.close()
    print("🔌 All connections closed.")
