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
    config_main = util.get_config('config_main.py')

    if not path.exists(config_main.LOG_DIR):
        makedirs(config_main.LOG_DIR, mode=0o755)

    if hasattr(config_main, 'LOG_FORMATTER'):
        logs.format_logs(formatter=config_main.LOG_FORMATTER)
    else:
        logs.format_logs(theme_color=config_main.TEXT_COLOR_THEME)

    if config_main.LOG_FILE:
        hdlr = logging.FileHandler(config_main.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        log.addHandler(hdlr)

    root_logger.setLevel(config_main.LOG_LEVEL)

    config_env = util.get_config('config_env.py')
    
   
    for e in config_env.ENV_LIST_ALL:
        log.debug(e)
        log.info("Building Environment: %s" % e.getEnvName())

        

if __name__ == "__main__":
    main()


