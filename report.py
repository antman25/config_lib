import logging
import collections

log = logging.getLogger(__name__)

def get_paths(source):
    paths = []
    if isinstance(source, collections.MutableMapping):  # found a dict-like structure...
        for k, v in source.items():  # iterate over it; Python 2.x: source.iteritems()
            paths.append([k])  # add the current child path
            paths += [[k] + x for x in get_paths(v)]  # get sub-paths, extend with the current
    # else, check if a list-like structure, remove if you don't want list paths included
    elif isinstance(source, collections.Sequence) and not isinstance(source, str):
        #                          Python 2.x: use basestring instead of str ^
        for i, v in enumerate(source):
            paths.append([i])
            paths += [[i] + x for x in get_paths(v)]  # get sub-paths, extend with the current
    return paths

def get_paths_withval(source):
    paths = []
    if isinstance(source, collections.MutableMapping):  # found a dict-like structure...
        for k, v in source.items():  # iterate over it; Python 2.x: source.iteritems()
            paths.append([(k, v)])  # add the current child path
            paths += [[k] + x for x in get_paths(v)]  # get sub-paths, extend with the current
    # else, check if a list-like structure, remove if you don't want list paths included
    elif isinstance(source, collections.Sequence) and not isinstance(source, str):
        #                          Python 2.x: use basestring instead of str ^
        for i, v in enumerate(source):
            paths.append([(i,v)])
            paths += [[i] + x for x in get_paths(v)]  # get sub-paths, extend with the current
    return paths

def traverse(dic, path=None):
    if not path:
        path=[]
    if isinstance(dic,dict):
        for x in dic.keys():
            local_path = path[:]
            local_path.append(x)
            for b in traverse(dic[x], local_path):
                 yield b
    elif isinstance(dic, collections.Sequence) and not isinstance(dic, str):
         for i in range(len(dic)):
            local_path = path[:]
            local_path.append(i)
            for b in traverse(dic[i], local_path):
                 yield b
    else: 
        yield path,dic

    
        
def generate_report(cfg_baseline, cfg_test):
    log.info("Generatating Report")
    unique_keys = []
    #log.debug(cfg_baseline)
#    ret = get_paths_withval(cfg_baseline['Env1'])
#    log.debug(ret)
    ret = traverse(cfg_baseline['Env1'])
    for c in ret:
        #cur = ret[i]
        log.debug(c)
    
