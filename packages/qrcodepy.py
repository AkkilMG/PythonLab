import qrcode

def CreateQR(name):
    data = input("Enter data to be converted to qrcode: ")
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save(f'{name}.png')
    print(f"Created {name} file")


if __name__ == "__main__":
    CreateQR(input("Enter filename: "))