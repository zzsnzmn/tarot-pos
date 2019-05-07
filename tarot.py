import random
import os
from sys import stdin
from escpos.printer import Usb

if __name__ == '__main__':
    p = Usb(0x0416, 0x5011) #, 0, profile="TM-T88III")
    image = 'images/'+random.choice(os.listdir('images'))
    p.image(image)
    p.text("\n\n\n\n")
