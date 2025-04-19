import qrcode

# Data to be encoded
data = "https://example.com"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls size of the QR Code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # size of each box in the QR code
    border=4,  # thickness of the border (default is 4)
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
