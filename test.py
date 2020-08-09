#!/usr/bin/python3
from os import path, makedirs

import logging
import json
import sys

import util
from errbot.logs import root_logger
import logs

log = logging.getLogger(__name__)
HERE = path.dirname(path.abspath(__file__))

def main():
    logs.format_logs()
    config = util.get_config('config_main.py')

    if not path.exists(config.LOG_DIR):
        makedirs(config.LOG_DIR, mode=0o755)

    if hasattr(config, 'LOG_FORMATTER'):
        logs.format_logs(formatter=config.LOG_FORMATTER)
    else:
        logs.format_logs(theme_color=config.TEXT_COLOR_THEME)

    if config.LOG_FILE:
        hdlr = logging.FileHandler(config.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        log.addHandler(hdlr)

    root_logger.setLevel(config.LOG_LEVEL)
  
    for e in config.ENV_LIST_ALL:
        log.debug(str(e))
        log.info("Building Environment: %s" % e.getEnvName())

        

if __name__ == "__main__":
    main()


