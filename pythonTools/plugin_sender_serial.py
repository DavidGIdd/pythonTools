import serial
import time

# SERIAL CONFIGURATION
PORT = "COM5"         # Change this to match your serial port
BAUD_RATE = 9600
TIMEOUT = 1

# OPEN SERIAL CONNECTION
try:
    ser = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)
    print(f"🟢 Connected to {PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    print(f"❌ Error opening serial port: {e}")
    exit()

# READ LINES FROM FILE (SAME AS IN YOUR TCP SCRIPT)
with open("loratestdata.txt", "r", encoding="utf-8") as f:
    lines = [
        line.strip().split(" ", 3)[-1] + "\r\n"
        for line in f if "," in line
    ]

# SEND LINES OVER SERIAL PORT
try:
    for line in lines:
        ser.write(line.encode('utf-8'))
        print(f"📤 Sent: {line.strip()}")
        time.sleep(1)  # Delay between lines (same as in TCP version)
except KeyboardInterrupt:
    print("⛔ Interrupted by user.")
finally:
    ser.close()
    print("🔌 Serial connection closed.")
