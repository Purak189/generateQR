import qrcode
from PIL import Image

# Configuración del contenido del QR y el logo
qr_content = "url"  # Cambia por el contenido que desees
logo_path = "tiktok.png"  # Ruta al archivo de imagen del logo
output_path = "qr_con_logo.png"  # Archivo de salida

# Generar el QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR (1 es el más pequeño, hasta 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada cuadro del QR
    border=4,  # Tamaño del borde
)

qr.add_data(qr_content)
qr.make(fit=True)

# Crear la imagen del QR
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Abrir el logo y redimensionarlo para que encaje en el QR
logo = Image.open(logo_path)

# Ajustar el tamaño del logo
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.2)  # Tamaño del logo como 20% del QR
logo = logo.resize((logo_size, logo_size))

# Pegar el logo en el centro del QR
logo_position = (
    (qr_width - logo_size) // 2,
    (qr_height - logo_size) // 2
)
qr_img.paste(logo, logo_position, mask=logo)

# Guardar el QR con el logo
qr_img.save(output_path)
print(f"Código QR guardado en {output_path}")
