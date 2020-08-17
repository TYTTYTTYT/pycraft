# -*- coding: utf-8 -*-

import config
from subprocess import Popen, PIPE
from threading import Thread


class GameServer(object):
    def __init__(self):
        self.all_log = []
        self.current_log = ''
        self.game = None
        self.listening_thread = None

    def start(self):
        self.game = Popen(
            config.GAME_COMMAND,
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE
        )
        self.listening_thread = Thread(target=self.listen)
        self.listening_thread.start()

    def setHandler(self, handler):
        self.handler = handler

    def stop(self):
        while self.game.poll() is None:
            self.game.stdin.write('/stop\n'.encode('utf-8'))
            self.game.stdin.flush()

    def listen(self):
        while self.isRunning():
            new_log = self.game.stdout.readline()
            self.current_log = new_log
            self.handler(new_log)

    def send(self, command):
        command = command + '\n'
        self.game.stdin.write(command.encode('utf-8'))
        self.game.stdin.flush()

    def isRunning(self):
        if self.game.poll() is not None:
            return False
        else:
            return True
