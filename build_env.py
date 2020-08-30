import logging
from jinja2 import Environment, FileSystemLoader
from lib.common import HostName, TagList
from lib.util import get_config
import json


log = logging.getLogger(__name__)

def buildCommonConfig():
    common_env = dict()
    ports = get_config('templates/constants/ports/all_ports.json')
    common_env.update(ports)
    tags = get_config('templates/constants/tags/all_tags.json')
    common_env.update(tags)

    log.debug("Common Tags: %s" % common_env)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('common.conf.jinja')

    common_conf = template.render(linux_tags=common_env)
    print ("Rendered Result: %s" % common_conf)

    return json.loads(common_conf)


def buildEnvConfig(env_name, scd_data, config_main, config_env, **extra_opts):
    log.info("Building config for %s" % env_name)
    env = Environment(loader=FileSystemLoader('templates'))
    #log.debug(scd_data)





