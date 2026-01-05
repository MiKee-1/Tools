import qrcode
from PIL import Image

# File paths
logo_path = "the path of logo you want in the center of the qr code" #/path/to/logo.png
qr_data = "your website here"
qr_output_path = "output path"

# Generate basic QR code
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High correction to allow for logo overlay
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)

# Create QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load and resize logo
logo = Image.open(logo_path)
logo_size = 150  # Size of logo to fit in the center, you can change it
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate position for logo placement
qr_width, qr_height = qr_img.size
logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2) 

# Paste the logo into the QR code
qr_img.paste(logo, logo_pos, mask=logo if logo.mode == 'RGBA' else None)

# Save the final QR code image
qr_img.save(qr_output_path)

qr_output_path
