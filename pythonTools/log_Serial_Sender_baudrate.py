import serial
import time

# === CONFIGURACIÓN ===
PORT = 'COM1'  # ⚠️ Cambia esto según tu sistema ('COMx' en Windows, '/dev/ttyUSBx' en Linux)
BAUDRATE = 921600  # Puedes subirlo más si tu adaptador lo soporta (hasta 3 Mbps o más)
LOG_FILE = 'data.log'  # Archivo de entrada con los datos
DELAY_BETWEEN_LINES = 0.01  # En segundos, entre líneas. Usa 0 para enviar lo más rápido posible

def send_file_over_serial(port, baudrate, filename, delay=0.0):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser:
            print(f"[INFO] Abierto {port} a {baudrate} bps.")
            with open(filename, 'r') as f:
                for line in f:
                    clean_line = line.strip()
                    if clean_line:
                        ser.write((clean_line + '\n').encode('utf-8'))
                        print(f"[TX] {clean_line}")
                        if delay > 0:
                            time.sleep(delay)
            print("[✓] Archivo enviado completamente.")
    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == '__main__':
    send_file_over_serial(PORT, BAUDRATE, LOG_FILE, DELAY_BETWEEN_LINES)
