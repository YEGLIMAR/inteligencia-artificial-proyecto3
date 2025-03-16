import qrcode
import os

# Lista de 10 códigos QR válidos (URLs correctas)
valid_qrs = [
    
    "https://google.com",
    "https://github.com",
    "https://openai.com",
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.tesla.com",
    "https://www.nasa.gov",
    "https://flutter.dev"
]

# Lista de 10 códigos QR inválidos (texto aleatorio y URLs mal formateadas)
invalid_qrs = [
    "htp://invalid-url",
    "random_text",
    "123456",
    "www.missing-http.com",
    "invalid.email@com",
    "ftp://wrongprotocol.com",
    "http//missing-colon.com",
    "!@#$%^&*()",
    "onlyspaces    ",
    "https://with space.com"
]

def generate_qr(data: str, filename: str):
    """Genera un código QR y lo guarda en un archivo"""
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR code saved: {filename}")

if __name__ == "__main__":
    qr_folder = "examples/"
    os.makedirs(qr_folder, exist_ok=True)

    # Generar QR válidos
    for i, qr_content in enumerate(valid_qrs):
        generate_qr(qr_content, f"{qr_folder}valid_qr_{i}.png")

    # Generar QR inválidos
    for i, qr_content in enumerate(invalid_qrs):
        generate_qr(qr_content, f"{qr_folder}invalid_qr_{i}.png")

