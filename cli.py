#!/usr/bin/python3 
import argparse
import logging
import os
import sys
from os import path, sep, getcwd, access, W_OK, makedirs
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

    for cur_path in config_main.ALL_DIRS:
        if not path.exists(cur_path):    
            makedirs(cur_path, mode=0o755)

    if hasattr(config_main, 'LOG_FORMATTER'):
        logs.format_logs(formatter=config_main.LOG_FORMATTER)
    else:
        logs.format_logs(theme_color=config_main.TEXT_COLOR_THEME)

    if config_main.LOG_FILE:
        hdlr = logging.FileHandler(config_main.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        root_logger.addHandler(hdlr)

    if args['verbose']:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(config_main.LOG_LEVEL)



    config_env = util.get_config(execution_dir + '/config_env.py')
    for e in config_env.ENV_LIST_ALL:
        baseline_scd_dir = config_main.SCD_BASELINE_DIR + '/' + e.env_name
        testing_scd_dir = config_main.SCD_TEST_DIR + '/' + e.env_name

        if not path.exists(baseline_scd_dir):
            makedirs(baseline_scd_dir, mode=0o755)
        if not path.exists(testing_scd_dir):
            makedirs(testing_scd_dir, mode=0o755)


    config_ports = util.get_config(execution_dir + '/config_ports.py')
    
    if args['list']:
        log.info("Listing all Environments")
        for e in config_env.ENV_LIST_ALL:
            log.info(repr(e))
            log.debug("Test %s" % e.env_name)

    env1_conf = util.get_config(config_main.CFG_BASELINE_DIR + '/Env1.conf')
    log.debug("Raw Config: %s" % str(env1_conf))
    log.debug("Env Name Test: %s" % env1_conf.env_name)


if __name__ == "__main__":

    main()
