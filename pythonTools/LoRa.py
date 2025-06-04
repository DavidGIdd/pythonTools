

import serial
import time

# Serial port settings
PORT = "COM12"  # Replace with your serial port (e.g., COM3 on Windows, /dev/tty.usbmodem58750025271 on MAC )
BAUD_RATE = 9600     # Default baud rate for Waveshare USB to LoRa
TIMEOUT = 1              # Timeout for serial communication in seconds

FILE_PATH = "loratestdata.txt"

ANTENNA_CHANNEL = "18"

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
        "Address": "AT+ADDR?",
        "Transmit Channel": "AT+TXCH?",
        "Receive Channel": "AT+RXCH?",
        "COM Baud Rate": "AT+BAUD?",
        "COM Mode": "AT+COMM?",
        "Power": "AT+PWR?",
        "Spreading Factor": "AT+SF?",
        "Bandwidth": "AT+BW?",
        "Error Coding": "AT+CR?",
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


def set_config(ser):
    print("\n--- Setting Device Configuration ---")
    commands = {
        "Spreading Factor": "AT+SF=5",
        "Power": "AT+PWR=22",
        "Coding Rate": "AT+CR=1", #1 represents 4/5, 2 represents 4/6, 3 represents 4/7, 4 represents 4/8
        "Baud Rate": "AT+BAUD=9600",
        "Transmit Channel": "AT+TXCH=18",
        "Receive Channel": "AT+RXCH=18"

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


def send_message_new(message, ser):
    print(f"\n--- Sending Message - {message}---")
    if ser and ser.is_open:
        chunk_size = 40  # safe chunk size for plugin
        for i in range(0, len(message), chunk_size):
            chunk = message[i:i + chunk_size]
            ser.write(chunk.encode('utf-8'))
            time.sleep(0.05)  # short pause between chunks

        # Send final newline so plugin's ReadLine() completes
        ser.write(b"\n")



def send_data(ser):
    print("\n--- Sending Data ---")
    a = 1
    b = 2
    c = 3
    while True:
        # message = f"{a},{b},{c}"
        message = f"{ANTENNA_CHANNEL}{a},846.0000,0.3290,0,0.0000,-3743.9900,912.2596,50.0000,0.0000,0.0000,0.0000,0.0000,0.0000,319.2927,905.2473,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,769.0000,0.0000,0.1828,846.0000,0.0000,0.1462"
        # message = f"{a}"
        send_message(message,ser)
        a += 1
        b += 1
        c += 1
        time.sleep(1)

    send_at_command(ser, "AT+EXI")
# Close the serial connection

def send_data_new(ser):
    print("\n--- Sending Data ---")
    a = 1
    while True:
        message = f"Channel:{ANTENNA_CHANNEL},Data:{a},846.0000,0.3290,0,0.0000,-3743.9900,912.2596,50.0000,0.0000,0.0000,0.0000,0.0000,0.0000,319.2927,905.2473,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,0.0000,769.0000,0.0000,0.1828,846.0000,0.0000,0.1462"
        send_message(message, ser)
        a += 1
        time.sleep(1)  # adjust as needed
# Close the serial connection

def read_lines():
    """Read lines from file and return a loopable list."""
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]  # Remove empty lines
    return lines if lines else ["No data"]  # Default if file is empty

def send_data_from_txt(ser):
    print("\n--- Sending Data from txt file ---")

    lines = read_lines()
    index = 0  # Track current line position
    a = 1

    while True:
        # Get the current line and add the date & time

        message = f"{a},{lines[index]}"

        # Send message
        send_message(message, ser)
        a+=1
        time.sleep(1)

        # Move to the next line, loop back if at the end
        index = (index + 1) % len(lines)

        time.sleep(1)  # Send every second

    send_at_command(ser, "AT+EXI")
# Close the serial connection


def close_serial(ser):
    if ser and ser.is_open:
        ser.close()
        print("Serial connection closed.")

if __name__ == "__main__":
    # Initialize serial connection
    # serial_connection = init_serial(PORT, BAUD_RATE, TIMEOUT)
    serial_connection = init_serial(PORT, BAUD_RATE, TIMEOUT)

    if serial_connection:
        try:
            # Query the current configuration
            # query_config(serial_connection)
            # set_config(serial_connection)

            #send_message(f"message",serial_connection)
            #send_data(serial_connection)
            send_data_new(serial_connection)
            #send_data_from_txt(serial_connection)

        except KeyboardInterrupt:
            print("Interrupted by user.")
        finally:
            close_serial(serial_connection)