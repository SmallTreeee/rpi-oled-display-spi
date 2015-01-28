#IMPORT POTRZEBNYCH BIBLIOTEK
import gaugette.ssd1306
import time
import sys
from PIL import Image

#USTAWIENIE ZMIENNYCH
RESET_PIN = 5 #(GPIO 24)
DC_PIN    = 4 #(GPIO 23)

#ROZDZIELCZOSC
width = 128
height = 64

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

image = Image.open(sys.argv[1])
image_r = image.resize((width,height), Image.BICUBIC)
image_bw = image_r.convert("1")

for x in range(width):
        for y in range(height):
                led.draw_pixel(x,y,bool(int(image_bw.getpixel((x,y)))))

led.display()
