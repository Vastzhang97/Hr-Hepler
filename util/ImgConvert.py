from PIL import Image
import os


def convert_to_png(file_path):
    image_prefix_path = os.path.splitext(file)[0]
    image = Image.open(file_path)
    image.save(image_prefix_path + ".png")
    os.remove(file_path)


if __name__ == '__main__':
    file = r"C://Users/62526/Desktop/Test/CheckCode.gif"
    convert_to_png(file)
