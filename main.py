import urllib.request
import time
from PIL import Image
import pydirectinput
import pyperclip
image_name = input()
def clamp(x):
  return max(0, min(x, 255))
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def moveCursor(currentX,currentY,targetX,targetY,speed):
    if currentX < targetX:
        while currentX < targetX:
            currentX+=speed
            pydirectinput.moveTo(currentX,currentY)
    elif currentX > targetX:
        while currentX > targetX:
            currentX-=speed
            pydirectinput.moveTo(currentX,currentY)
    if currentY < targetY:
        while currentY < targetY:
            currentY+=speed
            pydirectinput.moveTo(currentX,currentY)
    elif currentY > targetY:
        while currentY > targetY:
            currentY-=speed
            pydirectinput.moveTo(currentX,currentY)

handle = Image.open(f"images/{image_name}")
image = handle.resize((32, 32)).convert("RGB")
image.show()
print("Image compiled")
time.sleep(6)
#print("Enter (0,0) position:")
#start_emma = (878,230)
start = (536,142)
width = 15
previous = (start[0]-6,start[1]-6)
reset = (860,650)
startX = 6 
startY = 30
for x in range(startX,32):
    for y in range(0,32):
        coordinate = x1,y1 = x, y
        print(coordinate)
        #color select
        time.sleep(0.2)
        moveCursor(860,650,864,655,10)
        time.sleep(0.2)
        pydirectinput.click()
        #hex code
        moveCursor(864,655,866,590,10)
        pydirectinput.click()
        pydirectinput.typewrite(rgb2hex(image.getpixel(coordinate)[0],image.getpixel(coordinate)[1],image.getpixel(coordinate)[2]))
        pydirectinput.press('enter')
        #close
        moveCursor(866,590,864,655,10)
        pydirectinput.click()
        moveCursor(previous[0],previous[1],start[0]+(x*width),start[1]+(y*width),2)
        previous = (start[0]+(x*width),start[1]+(y*width))
        pydirectinput.click()
        if y == 31:
            previous = (previous[0],previous[1]-(width*31))
        #print(image.getpixel(coordinate))
