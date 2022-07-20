import urllib.request
from PIL import Image
import pyautogui
image_name = input()
def clamp(x):
  return max(0, min(x, 255))

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

handle = Image.open(f"images/{image_name}")
image = handle.resize((32, 32)).convert("RGB")

print("Image compiled")
#print("Enter (0,0) position:")
start = (878,230)
width = 26
for row in range(0,32):
    for column in range(0,32):
        coordinate = x,y = row, column
        #color select
        pyautogui.moveTo(1452,1117)
        pyautogui.click()
        #hex code
        pyautogui.click()
        pyautogui.write(rgb2hex(image.getpixel(coordinate)[0],image.getpixel(coordinate)[1],image.getpixel(coordinate)[2]))
        pyautogui.press('enter')
        #close
        pyautogui.moveTo(1771,725)
        pyautogui.click()
        
        pyautogui.moveTo(start[0]+(row*width),start[1]+(column*width))
        pyautogui.click()
        print(image.getpixel(coordinate))
