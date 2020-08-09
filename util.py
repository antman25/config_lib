import logging
import importlib
from os import path, makedirs
import time

log = logging.getLogger(__name__)

def get_config(config_path):
    log.info ('Loading: %s' % config_path)
    config_fullpath = config_path
    if not path.exists(config_fullpath):
        log.error('I cannot find the config file %s.' % config_fullpath)
        return None
    try:
        config = __import__(path.splitext(path.basename(config_fullpath))[0])
        log.info('Config check passed...')
        log.debug('------ Dump of %s variables -------' % config_path)
        print_config(config_path,config)
        return config
    except Exception:
        log.exception('I could not import your config from %s, please check the error below...' % config_fullpath)
        return None

def combineOptions(*args):
    result = {}
    for a in args:
        result.update(a)
    #log.debug("<combineOptions> Combined Result: %s" % str(result))
    return result

def print_config(config_name, config):
    for att in dir(config):
        if ('__' not in att):
            val = getattr(config,att)
            if isinstance(val, (str,int,list,dict,float)):
                log.debug("[%s] %s = %s" % (config_name, att, str(val)))
            #else:
            #    log.debug("[%s] %s = %s" % (config_name, att, type(val)))


