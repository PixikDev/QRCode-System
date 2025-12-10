import qrcode
import sys

def create_qr_from_link(link, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR-код сохранён как {filename}")

def main():
    if len(sys.argv) > 1:
        link = sys.argv[1]
    else:
        print("Введите ссылку для создания QR-кода: ")
        link = input()
    
    if link.strip():
        create_qr_from_link(link.strip())
    else:
        print("Ссылка не может быть пустой")

if __name__ == "__main__":
    main()