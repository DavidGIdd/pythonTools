import qrcode
from pathlib import Path

#THINGS THAT NEED TO BE CHANGED
product_name = 'Prompter'
purchase_link = 'https://a.co/d/b5NHzB6'
folder_for_qrcodes = r'C:\Users\DavidGarcía\Downloads\Macbackup\qrcodes'  # Use raw string
#ONLY THE product_name, purchase_link and folder_for_qrcodes

folder_path = Path(folder_for_qrcodes)

# Check if the folder exists
if folder_path.exists() and folder_path.is_dir():
    # Define the website link
    url = purchase_link
    # Generate the QR code
    qr = qrcode.make(url)
    # Save the QR code as an image file
    qr.save(folder_path / f'{product_name}.png')  # Use pathlib's join functionality

    print("QR code created successfully")
else:
    print(f"The folder '{folder_path}' does not exist.")
