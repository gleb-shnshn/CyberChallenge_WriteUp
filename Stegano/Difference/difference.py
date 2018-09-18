from PIL import Image

b=Image.open("bliss.bmp")
bn=Image.open("bliss_new.bmp")

a=""

for i in range(b.width):
    if b.getpixel((i,0))==bn.getpixel((i,0)):
        a+="0"
    else:
        a+="1"

print(a)

