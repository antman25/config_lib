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

    parser.add_argument('-l', '--list', action='store_true', help='list all available backends')

    #mode_selection = parser.add_mutually_exclusive_group()
    #mode_selection.add_argument('-i', '--init',
    #                            nargs='?',
    #                            default=None,
    #                            const='.',
    #                            help='Init stuff')
    #mode_selection.add_argument('-l', '--list', nargs='?', help='list all available backends')

    args = vars(parser.parse_args())
    print(args)

    config_main = util.get_config(execution_dir + '/config_main.py')  # will exit if load fails
    config_env = util.get_config(execution_dir + '/config_env.py')  # will exit if load fails
    
    if args['list']:
        print("Test")
        log.info("Listing all Environments")
        for e in config_env.ENV_LIST_ALL:
            log.info(e)


if __name__ == "__main__":

    main()
