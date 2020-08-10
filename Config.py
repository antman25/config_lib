import logging
#import copy


log = logging.getLogger(__name__)

class AttributeDict(dict):
    __slots__ = () 
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts):
    host = config_main.ARTIFACTORY_HOST
    port = config_main.ARTIFACTORY_PORT
    if env_name in ['Env1']:
        port = "8444"
    return { 'host' : host,
             'port' : port
            }        

def buildEnvConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['env_name'] = env_name

    result['artifactory'] = buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts)
    
    return result
