import logging
from AttributeDict import AttributeDict

log = logging.getLogger(__name__)

def buildFakeSCD(env_name, ip_start):
    linux_host_types = { 'linux_aa' : 2, 'linux_bb' : 2, 'linux_cc' : 1 } 

    windows_host_types = { 'win_dd' : 1, 'win_ee' : 1, 'win_ff' : 1}
        
    cur_ip = 1
    result = {}
    result['env_name'] = env_name    
    result['hosts'] = []
    for host_type in linux_host_types:
        log.debug("Build linux host type %s" % host_type)
        for i in range(linux_host_types[host_type]):
            host_name = env_name.lower() + '_' + host_type + '_'+ "{:02d}".format(i+1)
            result['hosts'].append({ 'hostname' : host_name,
                                     'ip' :  '10.' + str(ip_start) + '.0.' + "{:02d}".format(cur_ip),
                                     'os' : 'linux'
                                    })
            cur_ip += 1

    for host_type in windows_host_types:
        log.debug("Build windows host type %s" % host_type)
        for i in range(windows_host_types[host_type]):
            host_name = env_name.lower() + '_' + host_type + '_'+ "{:02d}".format(i+1)
            result['hosts'].append({ 'hostname' : host_name,
                                     'ip' :  '10.' + str(ip_start) + '.0.' + "{:02d}".format(cur_ip),
                                     'os' : 'windows'
                                    })
            cur_ip += 1


    return result
            
