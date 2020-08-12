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


        
def generate_report(cfg_baseline, cfg_test):
    log.info("Generatating Report")
    unique_keys = []
    #log.debug(cfg_baseline)
    ret = get_paths(cfg_baseline['Env1'])
    #log.debug(ret)
    for i in range(len(ret)):
        cur = ret[i]
        log.debug(cur)
    
