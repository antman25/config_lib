import logging
import time

CURRENT_TIME = time.strftime("%Y%m%d-%H%M%S")

DATA_DIR = '.'

LOG_DIR = DATA_DIR + '/logs'

CFG_DATA_DIR = DATA_DIR + '/cfg'
SCD_DATA_DIR = DATA_DIR + '/scd'

BASELINE_DIR = '/baseline'
TEST_DIR =  '/test'

CFG_BASELINE_DIR = CFG_DATA_DIR + BASELINE_DIR
CFG_TEST_DIR = CFG_DATA_DIR + TEST_DIR

SCD_BASELINE_DIR = SCD_DATA_DIR + BASELINE_DIR
SCD_TEST_DIR = SCD_DATA_DIR + TEST_DIR

ALL_DIRS = [LOG_DIR, CFG_DATA_DIR, CFG_BASELINE_DIR, CFG_TEST_DIR, SCD_DATA_DIR, SCD_BASELINE_DIR, SCD_TEST_DIR]

LOG_FILE = LOG_DIR + '/output_' + CURRENT_TIME + '.log'

LOG_LEVEL = logging.INFO

#LOG_FORMATTER = logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s")
TEXT_COLOR_THEME = 'light'


