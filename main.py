import argparse
import os
import qrcode

def generate_qr(url, output_dir="qr_codes", fill_color="black", back_color="white"):
    os.makedirs(output_dir, exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    filepath = os.path.join(output_dir, "qr_code.png")
    img.save(filepath)
    
    print(f"[SUCCESS] QR Code generated successfully!")
    print(f"[INFO] Target URL: {url}")
    print(f"[INFO] Saved location: {filepath}")
    return filepath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument("--url", type=str, default="http://github.com/kaw393939", help="URL to encode")
    args = parser.parse_args()

    fill_color = os.getenv("FILL_COLOR", "black")
    back_color = os.getenv("BACK_COLOR", "white")

    generate_qr(args.url, fill_color=fill_color, back_color=back_color)
