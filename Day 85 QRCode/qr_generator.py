import qrcode


def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    print(f"\n✅ QR Code saved as '{filename}'")


def main():
    print("=" * 40)
    print("        QR CODE GENERATOR")
    print("=" * 40)

    data = input("\nEnter text or URL: ").strip()

    if not data:
        print("Input cannot be empty!")
        return

    filename = input("Enter output file name (without extension): ").strip()

    if not filename:
        filename = "my_qrcode"

    generate_qr(data, filename + ".png")


if __name__ == "__main__":
    main()