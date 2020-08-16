# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('settings.txt')

GAME_COMMAND = config['Minecraft Settings']['game_command']
