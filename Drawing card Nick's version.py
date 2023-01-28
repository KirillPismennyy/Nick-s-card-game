from PIL import Image, ImageDraw, ImageFont

monsterName=input("What to draw?")
monsterHealthInsurance=input("What health does it have?")
width = 400
height = round(width / 0.715)
im = Image.new("RGB", (width,height))
im.save("Image1.png")

d = ImageDraw.Draw(im)
#fnt = ImageFont.truetype('arial.ttf', 50)
#get
d.text((0.75*width, 0.15*height),monsterName, fill=(255,255,55))
e = ImageDraw.Draw(im)
e.text((0.75*width, 0.14*height),"HP:", fill=(255,255,65))
f = ImageDraw.Draw(im)
f.text((0.78*width, 0.14*height),(monsterHealthInsurance), fill=(255,255,65))

im.show()

