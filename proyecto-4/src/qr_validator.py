import re

def validate_qr_content(content: str) -> bool:
    """
    Valida si el contenido del código QR es una URL válida.
    """
    url_pattern = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")
    if url_pattern.fullmatch(content):
        print("QR Code is a valid URL")
        return True
    print("QR Code is invalid")
    return False

if __name__ == "__main__":
    test_data = "https://example.com"
    validate_qr_content(test_data)
