from PIL import Image, ImageDraw, ImageFont

monsterName=input("What to draw?")
monsterHealthInsurance=input("What health does it have?")
monsterSocialStatus=input("What type does it have?")
monsterPrivilages=input("What strengths does it have?")
if monsterPrivilages==("none"):
    monsterFriends=input("What friends does it have?")
    if monsterFriends==("none"):
        monsterWhat=input("Does it even have anything?")
energyName=input("What energy type does it have?")

width = 400
height = round(width / 0.715)
im = Image.new("RGB", (width,height))
im.save("Image1.png")
#Hello, is this Nick's Burgers?
#I'm sorry, I just wanted a double cheeseburger
d = ImageDraw.Draw(im)
#get
fnt = ImageFont.truetype('arial.ttf', 10)
i = 10 #chage starting font here
while fnt.getsize("HP:")[0]+fnt.getsize(monsterHealthInsurance)[0] < 42:
    i = i + 1
    fnt = ImageFont.truetype('arial.ttf', i)
    print(i)
fnt = ImageFont.truetype('arial.ttf', i-1)

d.text((0.75*width, 0.12*height),monsterName, font=fnt, fill=(255,255,55))
e = ImageDraw.Draw(im)

height_of_name = fnt.getsize(monsterName)[1]
position = 0.14*height+fnt.getsize("HP:"+monsterHealthInsurance)[1]
e.text((0.75*width, position),"HP:"+monsterHealthInsurance, font=fnt, fill=(255,255,65))
height_of_name=fnt.getsize(monsterSocialStatus)[1]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
e.text((0.85*width, position),monsterSocialStatus, font=fnt, fill=(255,255,65))
position=0.94*height+fnt.getsize(monsterPrivilages)[1]
#new_im = Image.open("Pika.jpg")
poke_pic = Image.open("Pika.jpg")
# This resizes the picture without keeping scale ratio
poke_pic = poke_pic.resize((311,220))
#Pasting poke pic
im.paste(poke_pic, (50,100))

e.text((0.75*width, position), "Strenghts:" + monsterPrivilages, font=fnt, fill=(255,255,65))

x=257
y=528
z=0
symbol = Image.open(energyName + ".png")
# This keeps the scale, makes it "not bigger than"
symbol.thumbnail((32, 32))
# Pasting poke pic
im.paste(symbol, (x, y), symbol)

#f = ImageDraw.Draw(im)
#f.text((0.78*width, 0.14*height),(monsterHealthInsurance), font=fnt, fill=(255,255,65))
#we need moves, a type, strengths, weaknesses, abilities, and ditto
print("Done!")


    
im.show()
