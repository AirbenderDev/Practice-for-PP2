from PIL import Image


def is_png(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == "PNG"
    except Exception:
        return False


print(is_png("images/clock.png"))
print(is_png("images/mickeyclock.jpeg"))
print(is_png("images/min_hand.png"))
print(is_png("images/sec_hand.png"))
