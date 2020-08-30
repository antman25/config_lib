import logging

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


class Tag(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class TagList(object):
    def __init__(self, initial_values=None):
        if initial_values:
            self.tags = initial_values
        else:
            self.tags = {}

    def addTag(self, name, value):
        first_value_char = value[0]
        last_value_char = value[-1]

        if first_value_char == '<' and last_value_char != '>':
            raise ValueError("Invalid Value. Tag value - %s" % value)
        if first_value_char != '<' and last_value_char == '>':
            raise ValueError("Invalid Value. Tag value - %s" % value)

        if first_value_char == '<':
            value_tag_name = value[1:-1]
            self.__resolveValue(value_tag_name)

        if name not in self.tags:
            self.tags[name] = value
        else:
            raise ValueError("Attempted to add a duplicate tag name %s" % name)

    def __resolveValue(self, tag_name, tree=None):
        if not tree:
            tree = list()
        if tag_name in tree:
            raise ValueError("I think this might be recursive WOMP WOMP")
        if tag_name in self.tags:
            value = self.tags[tag_name]
            first_value_char = value[0]
            last_value_char = value[-1]

            if first_value_char == '<' and last_value_char != '>':
                raise ValueError("Invalid Value. Tag value - %s" % value)
            if first_value_char != '<' and last_value_char == '>':
                raise ValueError("Invalid Value. Tag value - %s" % value)
            if first_value_char == '<':
                value_tag_name = value[1:-1]
                tree.append(value_tag_name)
                print("Tree[%s] = %s" % (tag_name, tree))
                return self.__resolveValue(value_tag_name,tree)
            else:
                return value

        else:
            raise ValueError(
                "Attempted to access undefined tag %s. All defined tags: %s" % (tag_name, sorted(self.tags)))

    def getValue(self, tag_name, follow_ref=False):
        if tag_name in self.tags:
            if not follow_ref:
                return self.tags[tag_name]
            else:
                return self.__resolveValue(tag_name)
        else:
            raise ValueError("Attempted to access undefined tag %s. \
                              All defined tags: %s" % (tag_name, sorted(self.tags)))

    def __repr__(self):
        result = ""
        for tag_name in self.tags:
            result += "<%s> = %s\n" % (tag_name, self.tags[tag_name])
        return result


if __name__ == '__main__':
    start_val = dict(TAG1='Val1', TAG2='<TAG1>')
    tags = TagList(start_val)
    tags.addTag("TAG3", "Val3")
    tags.addTag("TAG5", "VAL")
    tags.addTag("TAG4", "<TAG5>")

    tags.addTag("TAG5", "VALAAA")
    print(tags)

    #print("TAG3 = %s" % tags.getValue("TAG3", False))
    #print("TAG4 = %s" % tags.getValue("TAG4", False))
    #print("TAG4 = %s" % tags.getValue("TAG4", True))

'''
def build_artifactory_connection(env_name, scd, config_main, config_env, **env_opts):
    host = config_main.ARTIFACTORY_HOST
    port = config_main.ARTIFACTORY_PORT
    if env_name in ['Env1']:
        port = "8444"
    return {'host': host,
            'port': port
            }


def buildHostGroup(scd, host_type):
    result = []
    for cur_host in scd.hosts:
        if cur_host.os == host_type:
            h = HostName(cur_host.hostname)
            if h.host_type not in result:
                result.append(h.host_type)
    return result


def buildHost(scd, host_type):
    result = []
    for cur_host in scd.hosts:
        if cur_host.os == host_type:
            h = HostName(cur_host.hostname)
            result.append({h.host_type + h.host_id: cur_host})
    return result


def buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['host_groups'] = buildHostGroup(scd, 'windows')
    result['hosts'] = buildHost(scd, 'windows')
    return result


def buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['host_groups'] = buildHostGroup(scd, 'linux')
    result['hosts'] = buildHost(scd, 'linux')
    return result


def buildEnvConfig(env_name, scd, config_main, config_env, **env_opts):
    result = AttributeDict()
    result['env_name'] = env_name

    result['artifactory'] = build_artifactory_connection(env_name, scd, config_main, config_env, **env_opts)

    result['linux'] = buildLinuxConfig(env_name, scd, config_main, config_env, **env_opts)
    result['windows'] = buildWindowsConfig(env_name, scd, config_main, config_env, **env_opts)
    return result
'''
