import sys, time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import numpy as np

import socketio

sio = socketio.Client()


width = 128
height = 64


def createImage():
    return Image.new('1', (width, height))


def sendImage(img):
    xp = np.packbits(np.array(img, dtype=np.uint8))
    xp = np.array(xp).tolist()
    sio.send(xp)

def quit():
    time.sleep(1)
    sio.disconnect()
    sys.exit()


@sio.event
def connect():
    print("Liboled connected.")

sio.connect('http://...:8080')