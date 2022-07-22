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
input("confirm")
print("Image compiled")
time.sleep(6)
#print("Enter (0,0) position:")
#start_emma = (878,230)
width = 20
#previous = (start[0]-6,start[1]-6)
startX = 0
#startY = 30
#color_speed = 10
#start = (536,142)
#color_select = (860,650)
#hex_select = (866,590)
color_speed = 1
start = (1067,190)
color_select = (1509,878)
hex_select = (1509,792)
#reset = (860,650-color_speed)
for x in range(startX,32):
    for y in range(0,32):
        coordinate = x1,y1 = x, y
        print(coordinate)
        #color select
        moveCursor(color_select[0],color_select[1]-(color_speed*4),color_select[0],color_select[1],color_speed)
        time.sleep(0.1)
        pydirectinput.click()
        #hex code
        moveCursor(hex_select[0],hex_select[1]-(color_speed*4),hex_select[0],hex_select[1],color_speed)
        pydirectinput.click()
        pydirectinput.typewrite(rgb2hex(image.getpixel(coordinate)[0],image.getpixel(coordinate)[1],image.getpixel(coordinate)[2]))
        pydirectinput.press('enter')
        #close
        moveCursor(color_select[0],color_select[1]-(color_speed*4),color_select[0],color_select[1],color_speed)
        pydirectinput.click()
        #moveCursor(previous[0],previous[1],start[0]+(x*width),start[1]+(y*width),2)
        moveCursor(start[0]+(x*width)-3,start[1]+(y*width),start[0]+(x*width)+2,start[1]+(y*width),1)
        #previous = (start[0]+(x*width),start[1]+(y*width))
        pydirectinput.click()
        #if y == 31:
            #previous = (previous[0],previous[1]-(width*31))
        #print(image.getpixel(coordinate))
