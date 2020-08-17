# -*- coding: utf-8 -*-

import sys
import os
import time

path2here = os.path.dirname(os.path.realpath(__file__))
libPath = os.path.join(path2here, 'libs')

sys.path.append(path2here)
sys.path.append(libPath)
os.chdir(path2here)

import config
from gameserver import GameServer
print(config.GAME_COMMAND)


def simpleHandler(msg):
    msg = msg.decode('utf-8')
    print(msg)
    print('simpleHandled')
    return


if __name__ == '__main__':
    game_server = GameServer()
    game_server.setHandler(simpleHandler)
    game_server.start()

    for i in range(5):
        time.sleep(1)
        game_server.send('hahaha')

    game_server.send('/stop')

    game_server.game.wait()
