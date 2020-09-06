import logging
from jinja2 import Environment, FileSystemLoader
from lib.common import HostName, TagList, HostList
from lib.util import get_config
import json

log = logging.getLogger(__name__)

def formatJson(data):
    print("FormatJson - Data = %s" % str(data))
    j = json.loads(data)
    return json.dumps(j,sort_keys=True,indent=4)

def buildCommonConfig():
    common_env = dict()
    ports = get_config('templates/constants/ports/all_ports.json')
    common_env.update(ports)
    linux_tags = get_config('templates/constants/tags/all_linux_tags.json')
    common_env.update(linux_tags)

    windows_tags = get_config('templates/constants/tags/all_windows_tags.json')

    log.debug("Common Tags: %s" % common_env)

    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True,lstrip_blocks=True,keep_trailing_newline=True)
    env.filters['jsonify'] = formatJson
    #env.filters['json_load'] = json.loads


    template = env.get_template('common.conf.jinja')

    common_conf = template.render(linux_tags=TagList(common_env), windows_tags=TagList(windows_tags))
    log.debug("Rendered Result:\n%s" % common_conf)

    return json.loads(common_conf)


def buildEnvConfig(env_name, scd_data, config_main, config_env, **extra_opts):
    log.info("Building config for %s" % env_name)
    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True,lstrip_blocks=True)
    env.filters['json_dump'] = json.dumps
    env.filters['json_load'] = json.loads

    template = env.get_template('env.conf.jinja')
    #env_conf = template.render(scd_data=scd_data, host_data=HostList(scd_data))
    #log.debug("Rendered Result:\n%s" % env_conf)
    #return json.loads(env_conf)
