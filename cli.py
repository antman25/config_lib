#!/usr/bin/python3 
import argparse
import logging
import os
import sys
from os import path, sep, getcwd, access, W_OK
from pathlib import Path

import logs
import util
from logs import root_logger

log = logging.getLogger(__name__)

def main():
    logs.format_logs(theme_color='light')
    execution_dir = getcwd()
    sys.path.insert(0, execution_dir)

    parser = argparse.ArgumentParser(description='The main entry point of the config builder.')

    parser.add_argument('-l', '--list', action='store_true', help='list all available backends')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable Verbose')

    args = vars(parser.parse_args())

    config_main = util.get_config(execution_dir + '/config_main.py')

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

    if args['verbose']:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(config_main.LOG_LEVEL)



    config_env = util.get_config(execution_dir + '/config_env.py')
    config_ports = util.get_config(execution_dir + '/config_ports.py')
    
    if args['list']:
        log.info("Listing all Environments")
        for e in config_env.ENV_LIST_ALL:
            log.info(repr(e))
            log.debug("Test %s" % e.env_name)


if __name__ == "__main__":

    main()
