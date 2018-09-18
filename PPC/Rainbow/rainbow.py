import colorsys
from PIL import Image

def get_hsv(hexrgb):
    hexrgb=hexrgb[0]
    hexrgb = hexrgb.lstrip("#")
    r, g, b = (int(hexrgb[i:i+2], 16) / 255.0 for i in range(0,5,2))
    return colorsys.rgb_to_hsv(r, g, b)


img = Image.new('RGBA', (44*128, 224))

def get_hex_from_rgb(t):
    a=hex(t[0])[2:]
    a=(2-len(a))*"0"+a
    b=hex(t[1])[2:]
    b=(2-len(b))*"0"+b
    c=hex(t[2])[2:]
    c=(2-len(c))*"0"+c
    return a+b+c

color_list=[]

for i in range(0,128):
    img1=Image.open("pieces/"+str(i)+".png")
    color_list.append((get_hex_from_rgb(img1.getpixel((20,20))),i))
color_list.sort(key=get_hsv)

k=0

for i in color_list:
    img2=Image.open("pieces/"+str(i[1])+".png")
    img.paste(img2, (44*k,0))
    k+=1
img.save("final.png")
