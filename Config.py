class EnvConfig(BaseConfig):
    def __init__(self, env):
        pass

    def get_config_object(self):
        pass

class BaseConfig():
    def get_config_object(self):
        raise NotImplementedError("getConfig function not defined")
