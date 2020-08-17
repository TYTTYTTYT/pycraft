# -*- coding: utf-8 -*-

import sys
from threading import Thread


def reflex():
    while True:
        line = sys.stdin.readline()
        if line == '/stop\n':
            break
        line = line + 'received'
        print(line, flush=True)
        
    return


if __name__ == '__main__':
    reflex_thread = Thread(target=reflex)
    reflex_thread.start()
    reflex_thread.join()
