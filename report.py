import logging
import collections
import util

log = logging.getLogger(__name__)

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
            local_path.append(str(i))
            for b in traverse(dic[i], local_path):
                 yield b
    else: 
        yield path,dic

    
        
def generate_report(cfg_baseline, cfg_test):
    log.info("Generatating Report")
    report_data = {}
    env_list = []
    for env_name in cfg_baseline:
        env_list.append(env_name)
        env_data = traverse(cfg_baseline[env_name])
        for path, value in env_data:
            #log.debug("CurPath: %s" % path)
            pretty_path = ".".join(path)
            #log.debug("%s = %s" % (pretty_path,value))
            if pretty_path not in report_data:
                report_data[pretty_path] = {}
            report_data[pretty_path][env_name] = value
    env_list = sorted(env_list)
    f = open('report.csv', 'w')
    #pretty_report = traverse(report_data)
    report_paths = sorted(list(report_data.keys()))
    f.write("Path," + ",".join(env_list) + "\n")
    for cur_path in report_paths:
        #log.debug("%s = %s" % (cur_path, report_data[cur_path]))
        output = [cur_path]
        for cur_env in env_list:
            if cur_env in report_data[cur_path]:
                output.append(report_data[cur_path][cur_env])
            else:
                output.append("UNDEFINED")
        f.write(",".join(output)+ "\n")
    f.close()
            
    

    #for path in report_data:
    #    for env in report_data[path]:
    #        if env not in report_data[path]:
    #            report_paths.append(path)
    #    log.debug("%s = %s" % (pretty_path,value))
    #log.debug("Report paths %s" % report_paths)
    
