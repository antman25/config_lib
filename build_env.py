import logging
from jinja2 import Environment, FileSystemLoader
from lib.common import HostName, TagList

log = logging.getLogger(__name__)

def buildEnvConfig(env_name, scd_data, config_main, config_env, **extra_opts):
    pass