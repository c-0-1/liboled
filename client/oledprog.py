from liboled import createImage, sendImage, width, height, quit

import sys, time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


from datetime import datetime



while True:
    try:
        im = createImage()
        drw = ImageDraw.Draw(im)
        drw.rectangle((0,0,width,height), fill=0)
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        drw.text((0,0), current_time, fill=255)
        sendImage(im)
        time.sleep(1)
    except KeyboardInterrupt:
        quit()
        sys.exit()
