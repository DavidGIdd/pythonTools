

import serial
import time

# Serial port settings
PORT = "COM4"  # Replace with your serial port (e.g., COM3 on Windows, /dev/tty.usbmodem58750025271 on MAC )
BAUD_RATE = 9600     # Default baud rate for Waveshare USB to LoRa
TIMEOUT = 1              # Timeout for serial communication in seconds

# Initialize the serial connection
def init_serial(port, baud_rate, timeout):
    try:
        # ser = serial.Serial(port, baud_rate, timeout=timeout)
        ser = serial.Serial(port, baud_rate, timeout=timeout)
        print(f"Connected to {port} at {baud_rate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

# Send an AT command and get the response
def send_at_command(ser, command):
    if ser and ser.is_open:
        try:
            ser.write((command + "\r\n").encode())  # Send the command with carriage return and newline
            time.sleep(0.1)  # Small delay to allow device to respond
            response = ser.read(ser.in_waiting or 1).decode().strip()  # Read available data
            return response
        except serial.SerialException as e:
            print(f"Error sending AT command: {e}")
            return None
    else:
        print("Serial connection is not open.")
        return None

# Query current configuration
def query_config(ser):
    print("\n--- Querying Device Configuration ---")
    commands = {
        "Spreading Factor": "AT+SF?",
        "Bandwidth": "AT+BW?",
        "Encoding Rate": "AT+CR?",
        "Power": "AT+PWR?",
        "Network ID": "AT+NETID?",
        "LBT Function": "AT+LBT?",
        "DTU Mode": "AT+MODE?",
        "Transmit Channel": "AT+TXCH?",
        "Receive Channel": "AT+RXCH?",
        "RSSI Signal Value": "AT+RSSI?",
        "Address": "AT+ADDR?",
        "COM Port": "AT+PORT?",
        "COM Baud Rate": "AT+BAUD?",
        "COM Mode": "AT+COMM?",
        "Error Coding": "AT+CR?",
    }
    response = send_at_command(ser, "+++")
    for key, command in commands.items():
        response = send_at_command(ser, command)
        if response:
            print(f"{key}:{response}")
        else:
            print(f"Failed to query {key}.")

    # Exit AT command mode (if required by the device)
    send_at_command(ser, "AT+EXIT")


def set_config(ser):
    print("\n--- Setting Device Configuration ---")
    commands = {
        "Spreading Factor": "AT+SF=12",
        "Bandwidth": "AT+BW=0",
        "Encoding Rate": "AT+CR=1",
        "Power": "AT+PWR=22",
        "Network ID": "AT+NETID=0",
        "LBT Function": "AT+LBT=0",
        "DTU Mode": "AT+MODE=1",
        "Transmit Channel": "AT+TXCH=18",
        "Receive Channel": "AT+RXCH=18",
        "RSSI Signal Value": "AT+RSSI=0",
        "Address": "AT+ADDR=0",
        "COM Port": "AT+PORT=3",
        "COM Baud Rate": "AT+BAUD=9600",
        "COM Mode": "AT+COMM=8N1"


    }
    response = send_at_command(ser, "+++")
    for key, command in commands.items():
        response = send_at_command(ser, command)
        if response:
            print(f"{key}: {response}")
        else:
            print(f"Failed to query {key}.")

    # Exit AT command mode (if required by the device)
    send_at_command(ser, "AT+EXI")

def send_message(message,ser):
    print(f"\n--- Sending Message - {message}---")
    response = send_at_command(ser, message)



def send_data(ser):
    print("\n--- Sending Data ---")
    a = 1
    b = 2
    c = 3
    while True:
        message = f"{a},{b},{c}"
        send_message(message,ser)
        a += 1
        b += 1
        c += 1
        time.sleep(1)

    send_at_command(ser, "AT+EXI")
# Close the serial connection
def close_serial(ser):
    if ser and ser.is_open:
        ser.close()
        print("Serial connection closed.")

if __name__ == "__main__":
    # Initialize serial connection
    serial_connection = init_serial(PORT, BAUD_RATE, TIMEOUT)
    # serial_connection = init_serial(PORT, TIMEOUT)

    if serial_connection:
        try:
            # Query the current configuration
            query_config(serial_connection)
            # set_config(serial_connection)

            #send_message(f"message",serial_connection)
            #send_data(serial_connection)

        except KeyboardInterrupt:
            print("Interrupted by user.")
        finally:
            close_serial(serial_connection)