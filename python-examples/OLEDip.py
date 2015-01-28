#IMPORT POTRZEBNYCH BIBLIOTEK
import gaugette.ssd1306
import time
import sys
import socket
import fcntl
import struct
from time import sleep

#FUNKCJA SPRAWDZAJACA ADRES IP
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

#USTAWIENIE ZMIENNYCH
RESET_PIN = 5 #(GPIO 24)
DC_PIN    = 4 #(GPIO 23)
TEXT = ''

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

#INFORMACJA ZWROTNA W ZALEZNOSCI OD STANU POLACZENIA
try:
    TEXT = get_ip_address('wlan0')
except IOError:
    try:
        TEXT = get_ip_address('eth0')
    except IOError:
        TEXT = ('NO INTERNET!')

led.clear_display()
led.draw_text2(0,25,TEXT,1)
led.draw_text2(0,0,"Witaj!",2)
led.draw_text2(0,16,"Twoj adres IP to:", 1)
led.display()
