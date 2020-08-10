import logging
from AttributeDict import AttributeDict

log = logging.getLogger(__name__)

def buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts):
    host = config_main.ARTIFACTORY_HOST
    port = config_main.ARTIFACTORY_PORT
    if env_name in ['Env1']:
        port = "8444"
    return { 'host' : host,
             'port' : port
            }

def buildHost(scd, host_type):
            

def buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['hosts'] = buildHost('windows')
    return result

def buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['hosts'] = buildHost('linux')
    return result

def buildEnvConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['env_name'] = env_name

    result['artifactory'] = buildArtifactoryConnection(env_name, scd, config_main, config_env, **env_opts)
    
    result['linux'] = buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts)
    result['windows'] = buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts)
    return result
