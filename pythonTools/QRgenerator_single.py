import qrcode
from pathlib import Path

product_name = 'SerialToEthernet'
purchase_link = 'https://a.co/d/ix7Evev'
folder_for_qrcodes = 'C:\\Users\\DavidGarcía\\Downloads\\Macbackup\\qrcodes'
folder_path = Path(f'{folder_for_qrcodes}')

# Check if the folder exists
if folder_path.exists() and folder_path.is_dir():
    # Define the website link
    url = f'{purchase_link}'
    # Generate the QR code
    qr = qrcode.make(url)
    # Save the QR code as an image file
    type(qr)
    qr.save(f'{folder_for_qrcodes}/{product_name}.png')

    print("QRcode created succesfully")
else:
    print(f"The folder '{folder_path}' does not exist.")
