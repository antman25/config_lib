import logging
from difflib import get_close_matches

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
        self.__tags = {}
        if initial_values:
            for tagName in initial_values:
                self.__updateTag(tagName, initial_values[tagName])

    def getAllTagNames(self):
        return sorted(self.__tags)

    @staticmethod
    def __checkValidTagName(name):
        if len(name) < 2:
            return False
        first_value_char = name[0]
        last_value_char = name[-1]
        if first_value_char == '<' and last_value_char == '>':
            return True
        if first_value_char == '<' and last_value_char != '>':
            return False
        if first_value_char != '<' and last_value_char == '>':
            return False
        return False

    @staticmethod
    def __getTagFromRef(name):
        if TagList.__checkValidTagName(name):
            return name[1:-1]
        return name

    def __updateTag(self, name, value):
        # check if the value is another tag
        # print ("addTag(%s, %s)" % (name,value))
        if TagList.__checkValidTagName(value):
            # print ("addTag - Value [%s] is a Tag Reference" % value)
            value_tag_name = TagList.__getTagFromRef(value)
            try:
                test_val = self.__getValue(value_tag_name, [name])
                # print("addTag - Test Val %s" % str(test_val))
            except KeyError as ex:
                print("WARN: Potentially undefined tag - %s" % ex)

        if name not in self.__tags:
            self.__tags[name] = value
        else:
            old_value = self.__tags[name]
            print("WARN: Updating the value of tag %s. Prev Val: %s -- New Val: %s" % (name, old_value, value))
            self.__tags[name] = value

    def __getValue(self, name, ref_tags=None, max_depth=0):
        # Check for circular references
        if name in ref_tags:
            raise RecursionError(
                "Tag %s has circular references. Tag Chain: %s" % (name, ' -> '.join(ref_tags + [name])))
        # Tag Exists
        if name in self.__tags:
            value = self.__tags[name]
            if max_depth == len(ref_tags):
                return value
            else:
                # Value is a Tag Reference
                if TagList.__checkValidTagName(value):
                    value_tag_name = TagList.__getTagFromRef(value)
                    return self.__getValue(value_tag_name, ref_tags + [name])
                else:
                    return value
        else:
            close_tags = get_close_matches(name, self.getAllTagNames())
            error = "Attempted to access undefined tag %s. " % name
            if len(close_tags) > 0:
                error += "Possible matches: %s" % close_tags
            else:
                error += "All known tags: %s" % sorted(self.__tags)
                raise KeyError(error)

    def getValue(self, name, follow_ref=False):
        if follow_ref:
            return self.__getValue(name, [], -1)
        return self.__getValue(name, [])

    def __repr__(self):
        result = ""
        for name in self.__tags:
            result += "<%s> = %s\n" % (name, self.__tags[name])
        return result

    def __getitem__(self, name):
        return self.__getValue(name, [])

    def __setitem__(self, key, value):
        self.__updateTag(key,value)

    def __iter__(self):
        return self.__tags.__iter__()


if __name__ == '__main__':
    start_val = dict(CoolTag='CoolVal',
                     TAG2='<TAG1>',
                     TAG1='ASDF',
                     BootLeg='Aasdfsdfff',
                     Turtle='asdffff',
                     TAGA='<TAGB>',
                     TAGB='<TAGC>',
                     TAGC='FFFF')

    tags = TagList(start_val)
    tags["TAGC"] = "<TAG!A>"
    tags["TAGDDDD"] = "<TAGA>"
    print("Accessing TAG3 = %s" % tags["TAGA"])
    print("Accessing TAG2 = %s" % tags.getValue("TAGA", False))

    all_tags = tags.getAllTagNames()

    # print(all_tags)
    print("-----------")
    for tag_name in all_tags:
        # print(tag_name)
        # print(tags[tag_name])
        print("Tag[%s] = %s" % (tag_name, tags[tag_name]))
    print("-----------")
    for tag_name in all_tags:
        # print(tag_name)
        # print(tags[tag_name])
        print("Tag[%s] = %s" % (tag_name, tags.getValue(tag_name, True)))
    print("-----------")
    for tag_name in tags:
        print("Tag[%s] = %s" % (tag_name,tags[tag_name]))

    # print(tags["TAg5"])

    # print("TAG3 = %s" % tags.getValue("TAG3", False))
    # print("TAG4 = %s" % tags.getValue("TAG4", False))

