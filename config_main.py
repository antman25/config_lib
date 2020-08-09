import logging
import time

CURRENT_TIME = time.strftime("%Y%m%d-%H%M%S")

DATA_DIR = '.'

LOG_DIR = DATA_DIR + '/logs'
LOG_FILE = LOG_DIR + '/output_' + CURRENT_TIME + '.log'

LOG_LEVEL = logging.INFO

#LOG_FORMATTER = logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s")
TEXT_COLOR_THEME = 'light'


