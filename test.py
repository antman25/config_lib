#!/usr/bin/python3
from os import path

import logging
import json
import sys

import util
from errbot.logs import root_logger
import logs

log = logging.getLogger(__name__)
HERE = path.dirname(path.abspath(__file__))

if __name__ == '__main__':
    logs.format_logs()
    config = util.get_config('config.py')

    if hasattr(config, 'LOG_FORMATTER'):
        logs.format_logs(formatter=config.LOG_FORMATTER)
    else:
        logs.format_logs(theme_color=config.TEXT_COLOR_THEME)

    if config.LOG_FILE:
        hdlr = logging.FileHandler(config.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        log.addHandler(hdlr)

    log.setLevel(config.LOG_LEVEL)
    log.info("test")    
    log.debug("test")
    log.warning("Test")
    log.error("Asdf")
    log.critical("asdf")
    

