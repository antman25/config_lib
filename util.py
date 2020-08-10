import logging
import importlib
from os import path, makedirs
import time
import sys
import json
import Config

log = logging.getLogger(__name__)

def dict_raise_on_duplicates(ordered_pairs):
    d = Config.AttributeDict()
    for k, v in ordered_pairs:
        if k in d:
           raise ValueError("duplicate key: %r" % (k,))
        else:
           d[k] = v
    return d

def save_config(config_path, output):
    f = open(config_path, "w")
    j = json.dumps(output,indent=4, sort_keys=True)
    #print (j)
    f.write(j)
    f.close()
    

def get_config(config_path):
    log.info ('Loading: %s' % config_path)
    config_fullpath = config_path
    if not path.exists(config_fullpath):
        log.error('I cannot find the config file %s.' % config_fullpath)
        return None
    try:
        file_name, file_ext = path.splitext(path.basename(config_fullpath))
        config = None
        if file_ext == '.py':
            log.info('Importing Config %s' % file_name)
            config = __import__(file_name)
            log.debug('Config check passed...')
            log.debug('------ Dump of %s variables -------' % config_path)
            print_config(file_name,config)
            log.debug('------End Dump of %s variables -------' % config_path)
        elif file_ext in ['.conf', '.json']:
            f = open(config_fullpath)
            d = f.read()
            f.close()
            return json.loads(d, object_pairs_hook=dict_raise_on_duplicates)
        else:
            log.exception('Unknown File Type for path %s - Ext = %s' % (config_fullpath,file_ext))  
            sys.exit(-1)
        return config
    except Exception:
        log.exception('I could not import your config from %s, please check the error below...' % config_fullpath)
        sys.exit(-1)

def combineAttributes(*args):
    result = Config.AttributeDict()
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

