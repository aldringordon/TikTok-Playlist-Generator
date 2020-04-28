import pytesseract as tess
from PIL import Image

data_location = "../test_data/"
test_data = ["test1.png", "test2.png", "test3.png", "test4.png", "test5.png"]
images = [data_location + x for x in test_data]


for test_image in images:
    img = Image.open(test_image)
    text = tess.image_to_string(img)
    print("#####################")
    print("test image: " + test_image)
    print("---------------------")
    print(text)
    print("---------------------")
    print("text.size() = " + str(len(text)))
