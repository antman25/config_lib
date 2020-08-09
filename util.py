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
        p = path.splitext(path.basename(config_fullpath))[0]
        log.info('Importing Config %s' % p)
        config = __import__(p)
        log.debug('Config check passed...')
        log.debug('------ Dump of %s variables -------' % config_path)
        print_config(p,config)
        log.debug('------End Dump of %s variables -------' % config_path)
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
            if isinstance(val, (str,int,bool)):
                log.debug("%s.%s = %s -- Type: %s" % (config_name, att, str(val), type(val)))
            elif isinstance(val, list):
                log.debug("%s.%s = " % (config_name, att))
                log.debug("[")
                for it in val:
                    log.debug("\t%s -- Type: %s" % (str(it), type(it)))
                log.debug("]")
            elif isinstance(val, dict):
                log.debug("%s.%s = " % (config_name, att))
                log.debug("{")
                for it in val:
                    log.debug("\t%s : %s -- Type: %s" % (str(it), str(val[it]), type(val[it])))
                log.debug("}")

            #else:
            #    log.debug("[%s] %s = %s" % (config_name, att, type(val)))


