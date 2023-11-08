from PIL import Image

with Image.open("./test_image.jpg") as img:
    img = img.rotate(45)
    img.save("./test_image.jpg")