import cv2
from pyzbar.pyzbar import decode

def scan_qr_from_image(image_path: str):
    """Escanea un código QR desde una imagen y devuelve su contenido."""
    image = cv2.imread(image_path)
    detected_qrs = decode(image)

    if not detected_qrs:
        print(f"❌ No QR found in {image_path}")
        return None

    for qr in detected_qrs:
        decoded_text = qr.data.decode('utf-8')
        print(f"✅ Decoded QR from {image_path}: {decoded_text}")
        return decoded_text  # Devuelve el primer QR encontrado

def scan_qr_from_camera():
    """Escanea un código QR en tiempo real usando la cámara del dispositivo."""
    cap = cv2.VideoCapture(0)  # Usa la cámara predeterminada

    print("📸 Apunta la cámara al código QR y presiona 'q' para salir...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Error al acceder a la cámara.")
            break

        detected_qrs = decode(frame)

        for qr in detected_qrs:
            decoded_text = qr.data.decode('utf-8')
            print(f"✅ QR detectado: {decoded_text}")
            cap.release()
            cv2.destroyAllWindows()
            return decoded_text  # Detiene el escaneo tras leer un código

        cv2.imshow("Escaneo de QR - Presiona 'q' para salir", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

if __name__ == "__main__":
    mode = input("¿Quieres escanear desde (1) Imagen o (2) Cámara? [1/2]: ")

    if mode == "1":
        image_path = input("Ingresa el nombre del archivo de imagen desde la carpeta examples: ")
        scan_qr_from_image(image_path)
    elif mode == "2":
        scan_qr_from_camera()
    else:
        print("❌ Opción inválida. Elige 1 o 2.")
