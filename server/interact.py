import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import numpy as np

disp = Adafruit_SSD1306.SSD1306_128_64(rst=24)

disp.begin()
disp.clear()
disp.display()


def imagr(raw):
    bits = np.array(raw, dtype=np.uint8)
    image = np.unpackbits(np.array(bits))
    image = np.array(image)
    rotated = Image.fromarray(255 * image.reshape(64,128).view(np.uint8)).convert('1')
    return rotated

def disparray(ar):
    disp.image(ar)
    disp.display()
