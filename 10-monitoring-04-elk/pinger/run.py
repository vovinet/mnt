#!/usr/bin/env python3

import logging
import random
import time

while True:

    number = random.randrange(0, 4)

    if number == 0:
        logging.info('{ "logs": { "message": "Hello there!!" } }')
    elif number == 1:
        logging.warning('{ "logs": { "message": "Hmmm....something strange" } }')
    elif number == 2:
        logging.error('{"logs": { "message": "OH NO!!!!!!" } }')
    elif number == 3:
        logging.exception(Exception('{"logs": { "message": "this is exception" } }'))

    time.sleep(1)
