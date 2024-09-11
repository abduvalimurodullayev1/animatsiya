from wifi_qrcode_generator import wifi_qrcode

# WiFi ma'lumotlarini kiriting
wifi_data = wifi_qrcode("4545455", hidden=False, authentication_type="WPA", password="abuvali2006")

# QR kodni yaratish
qr_code_image = wifi_data.make_image()

# QR kodni saqlash
qr_code_image.save("wifi_qr_code.png")
