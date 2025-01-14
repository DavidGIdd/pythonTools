import serial

# Set up the serial connection
ser = serial.Serial(
    'COM3',         # Replace 'COM3' with the correct serial port for your device
    baudrate=9600,  # Set the baud rate to match your device
    timeout=1       # Optional: sets the timeout for the connection (in seconds)
)

# Check if the serial port is open
if ser.is_open:
    print("Serial port is open")

# Send data
data_to_send = "Hello, device!\n"
ser.write(data_to_send.encode())  # .encode() converts the string to bytes

# Close the serial connection when done
ser.close()