import logging
from AttributeDict import AttributeDict

log = logging.getLogger(__name__)

class HostName(object):
    def __init__(self, hostname):
        self.__hostname = hostname
        self.__split_host = self.__hostname.split('_')
    
    @property
    def env_name(self):
        return self.__split_host[0] 

    @property
    def os(self):
        return self.__split_host[1]

    @property
    def host_type(self):
        return self.__split_host[2]

    @property
    def host_id(self):
        return self.__split_host[3]

def buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts):
    host = config_main.ARTIFACTORY_HOST
    port = config_main.ARTIFACTORY_PORT
    if env_name in ['Env1']:
        port = "8444"
    return { 'host' : host,
             'port' : port
            }



def buildHost(scd, host_type):
    result = []
    for cur_host in scd.hosts:
        if cur_host.os == host_type:
            h = HostName(cur_host.hostname)
            result.append( { h.host_type + h.host_id : cur_host})
    return result        

def buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['hosts'] = buildHost(scd, 'windows')
    return result

def buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['hosts'] = buildHost(scd, 'linux')
    return result

def buildEnvConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['env_name'] = env_name

    result['artifactory'] = buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts)
    
    result['linux'] = buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts)
    result['windows'] = buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts)
    return result
