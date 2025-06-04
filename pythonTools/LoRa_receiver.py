import serial
import time

# LoRa module serial port configuration
SERIAL_PORT = "COM4"  # Change to your actual port
BAUD_RATE = 9600
LOG_FILE = "lora_log.txt"

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Track last received sequence per sender
last_received_sequence = {}

print("Listening for incoming LoRa messages...")

try:
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:  # Use UTF-8 encoding
        while True:
            if ser.in_waiting:
                raw_data = ser.readline()
                raw_clean_data = raw_data.decode(errors="ignore").strip().strip('\x00').strip('\xe1')
                print(f"Raw Data: {raw_clean_data}")  # Debugging step

                log_file.flush()  # Ensure data is written to the file immediately

            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nReceiver stopped.")
    ser.close()
