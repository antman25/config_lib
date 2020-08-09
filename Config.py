import copy

class AttributeDict(dict):
    __slots__ = () 
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

class BaseConfig(object):
    def __init__(self, config = {}):
        self._config = config

    def __getattribute__(self, name):
    #    if name in self._config:
    #        return self._config[name]
        return super(BaseConfig, self).__getattribute__(name)

    def __add__(self, other):
        r = copy.deepcopy(self._config)
        r.update(other)
        return r

    def __iadd__(self, other):
        self._config = self + other
        return self._config

    def get_config_object(self):
        return self._config

class Tag(BaseConfig):
    def __init__(self, tag_name, tag_value):
        self.tag_name = tag_name
        self.tag_value = tag_value

    def getTagRef(self):
        return "<" + tag_name + ">"

    def get_config_object(self):
        return { tag_name : tag_value }

    def __repr__(self):
        return "Tag(%s,%s)" % (self.tag_name, self.tag_value)
    
    def __str__(self):
        return "Tag <%s> = %s" % (self.tag_name, self.tag_value)


class EnvConfig(BaseConfig):
    def __init__(self, env):
        pass

    def get_config_object(self):
        pass

class PortTag(Tag):
    def get_config_object(self):
        return { tag_name : str(tag_value) }



