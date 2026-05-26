import qrcode

# --- data to encode ---
data = "https://github.com/charanreddy0006"

# --- create QR code ---
qr = qrcode.make(data)

# --- save QR image ---
qr.save("github_qr.png")

print("QR Code generated successfully ✅")