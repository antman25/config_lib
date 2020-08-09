#!/usr/bin/python3 
import argparse
import logging
import os
import sys
from os import path, sep, getcwd, access, W_OK
from pathlib import Path

import logs
import util

log = logging.getLogger(__name__)

def main():
    logs.format_logs()
    execution_dir = getcwd()
    sys.path.insert(0, execution_dir)

    parser = argparse.ArgumentParser(description='The main entry point of the config builder.')

    parser.add_argument('-c', '--config', default=None,
                        help='Full path to your config')

    mode_selection = parser.add_mutually_exclusive_group()
    #mode_selection.add_argument('-i', '--init',
    #                            nargs='?',
    #                            default=None,
    #                            const='.',
    #                            help='Init stuff')
    mode_selection.add_argument('-l', '--list', nargs='?', help='list all available backends')

    args = vars(parser.parse_args())

    config_path = args['config']

    # setup the environment to be able to import the config.py
    if config_path:
        # appends the current config in order to find config.py
        sys.path.insert(0, path.dirname(path.abspath(config_path)))
    else:
        config_path = execution_dir + '/cfg/config_main.py'

    config_main = util.get_config(config_path)  # will exit if load fails
    
    
    if args['list']:
        log.info("Listing all Environments")
        for e in config_env.ENV_LIST_ALL:
            log.info(e)


if __name__ == "__main__":

    main()
