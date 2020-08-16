# -*- coding: utf-8 -*-

import time
import sys

for i in range(10):
    time.sleep(1)
    sys.stdout.write(str(i) + '\n')
    sys.stdout.flush()
