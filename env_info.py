import logging

log = logging.getLogger(__name__)

class EnvList(object):
    def __init__(self,env_list):
        self._env_list = {}
        #for 



class EnvInfo(object):
    def __init__(self, env_name, **env_opts):
        self._env_name = env_name
        self._env_opts = env_opts

    def getEnvOpt(self, option_name):
        if option_name in self._env_opts: 
            return self._env_opts[option_name]
        return None

    def __getattribute__(self, name):
        if name == 'env_name':
            return self._env_name
        #if name in self._env_opts:
        #    return self._env_opts[name]
        return super(EnvInfo, self).__getattribute__(name)

    def getEnvName(self):
        return self._env_name

    def getAllEnvOpts(self):
        return self._env_opts

    def getEnvType(self):
        return self.getEnvOpt('env_type')
    
    def getCloudFlag(self):
        return self.getEnvOpt('cloud_flag')

    def getSmallFlag(self):
        return self.getEnvOpt('small_flag')

    def getFeature1(self):
        return self.getEnvOpt('feature1_flag')

    def getFeature2(self):
        return self.getEnvOpt('feature2_flag')

    def __str__(self):
        #return "<EnvInfo> Name: %s Type: %s Cloud: %s Small: %s Feature1: %s Feature2: %s" % (self.getEnvName(), self.getEnvType(), self.getCloudFlag(), self.getSmallFlag(), self.getFeature1(), self.getFeature2())
	    return repr(self)

    def __repr__(self):
        return "EnvInfo(env_name=%s, env_opts=%s)" % (self.getEnvName(), self.getAllEnvOpts())
    
