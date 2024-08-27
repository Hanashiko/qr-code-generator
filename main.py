import qrcode
from qrcode.image.pil import PilImage
from qrcode.main import QRCode
input_text: str = input("Write your link or text: ")
qr: QRCode = qrcode.QRCode(
    version=3, 
    box_size=20, 
    border=10, 
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(input_text)
qr.make(fit=True)
image: PilImage = qr.make_image(fill_color="black",back_color="white")
file_name: str = "qr_code.png"
image.save(file_name)
print(f"Successful save qr-code as a file - {file_name}")