from interact import *
from interact import disparray, imagr

from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


@sio.on('message')
async def print_message(sid, message):
    disparray(imagr(message))


if __name__ == '__main__':
    web.run_app(app)
