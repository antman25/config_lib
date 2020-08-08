import logging
import importlib
from os import path, makedirs

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
        return config
    except Exception:
        log.exception('I could not import your config from %s, please check the error below...' % config_fullpath)
        return None
