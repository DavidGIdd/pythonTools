import qrcode
import os
import json

json_file_path = '/Users/davidgarcia/Downloads/productCATALOG.json'
folder_for_qrcodes = '/Users/davidgarcia/Desktop/qrcodes'

with open(json_file_path, 'r') as file:
    data = json.load(file)
    for x in data:
        # Define the website link
        url = f'{x['Purchase Link']}'
        # Generate the QR code
        qr = qrcode.make(url)
        # Save the QR code as an image file
        type(qr)
        qr.save(f'{folder_for_qrcodes}/{x['Product']}.png')

print("QRcode created succesfully")
