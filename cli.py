#!/usr/bin/python3 
import argparse
import logging
import sys
from os import path, getcwd, makedirs
from shutil import copyfile

from lib import logs, util
import report
import build_env
import build_scd

from lib.logs import root_logger
from lib.AttributeDict import AttributeDict

log = logging.getLogger(__name__)

def load_all_scd(config_main, config_env):
    baseline = AttributeDict()
    test = AttributeDict()
    for env_name in config_env.ENV_LIST_ALL:
        baseline_cfg_path = config_main.SCD_BASELINE_DIR + '/' + env_name + '/' 'data.json'
        test_cfg_path = config_main.SCD_TEST_DIR + '/' + env_name + '/' 'data.json'
        try:
            baseline[env_name] = util.get_config(baseline_cfg_path)
        except Exception as ex:
            log.error("Could not load %s - Caught Exception %s" % (baseline_cfg_path, ex))

        try:
            test[env_name] = util.get_config(test_cfg_path)
        except Exception as ex:
            log.error("Could not load %s - Caught Exception %s" % (test_cfg_path, ex))

    return baseline, test

def load_all_cfg(config_main,config_env):
    baseline = AttributeDict()
    test = AttributeDict()
    for env_name in config_env.ENV_LIST_ALL:
        baseline_cfg_path = config_main.CFG_BASELINE_DIR + '/' + env_name + '.conf'
        test_cfg_path = config_main.CFG_TEST_DIR + '/' + env_name + '.conf'
        
        try:
            baseline[env_name] = util.get_config(baseline_cfg_path)
        except Exception as ex:
            log.error("Could not load %s - Caught Exception %s" % (baseline_cfg_path, ex))

        try:
            test[env_name] = util.get_config(test_cfg_path)
        except Exception as ex:
            log.error("Could not load %s - Caught Exception %s" % (test_cfg_path, ex))
    return baseline, test

def main():
    logs.format_logs(theme_color='light')
    execution_dir = getcwd()
    sys.path.insert(0, execution_dir)

    parser = argparse.ArgumentParser(description='The main entry point of the config builder.')

    parser.add_argument('-l', '--list', action='store_true', help='list all available backends')
    parser.add_argument('-b', '--build', action='store_true', help='Build all configs')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable Verbose')
    parser.add_argument('-r', '--report', action='store_true', help='Generate Report')
    parser.add_argument('-f', '--fake', action='store_true', help='Generate Fake SCD')
    parser.add_argument('-p', '--promote', action='store_true', help='Copy test to baseline')

    args = vars(parser.parse_args())

    config_main = util.get_config(execution_dir + '/config_main.py')

    for cur_path in config_main.BUILD_DIRS:
        if not path.exists(cur_path):    
            makedirs(cur_path, mode=0o755)

    if hasattr(config_main, 'LOG_FORMATTER'):
        logs.format_logs(formatter=config_main.LOG_FORMATTER)
    else:
        logs.format_logs(theme_color=config_main.TEXT_COLOR_THEME)

    if config_main.LOG_FILE:
        hdlr = logging.FileHandler(config_main.LOG_FILE)
        hdlr.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(name)-25s %(message)s"))
        root_logger.addHandler(hdlr)

    if args['verbose']:
        root_logger.setLevel(logging.DEBUG)
    else:
        root_logger.setLevel(config_main.LOG_LEVEL)



    config_env = util.get_config(execution_dir + '/config_env.py')
    for env_name in config_env.ENV_LIST_ALL:
        baseline_scd_dir = config_main.SCD_BASELINE_DIR + '/' + env_name
        testing_scd_dir = config_main.SCD_TEST_DIR + '/' + env_name

        if not path.exists(baseline_scd_dir):
            makedirs(baseline_scd_dir, mode=0o755)
        if not path.exists(testing_scd_dir):
            makedirs(testing_scd_dir, mode=0o755)


    config_ports = util.get_config(execution_dir + '/config_ports.py')
    
    if args['list']:
        log.info("Listing all Environments")
        for env_name in config_env.ENV_LIST_ALL:
            data = config_env.ENV_LIST_ALL[env_name]
            log.info("EnvName: %s Env Attributes %s" % (env_name,str(data)))

    if args['build']:
        log.info("Loading all Baseline and Test SCD Files")
        scd_baseline, scd_test = load_all_scd(config_main, config_env)
        #log.debug("Loaded SCD Baseline: %s" % str(scd_baseline))
        #log.debug("Loaded SCD Test: %s" % str(scd_test))

        common_conf = build_env.buildCommonConfig()

        util.save_config(config_main.CFG_TEST_DIR + 'common.conf', common_conf)

        for env_name in config_env.ENV_LIST_ALL:
            env_opts = config_env.ENV_LIST_ALL[env_name]
            c = build_env.buildEnvConfig(env_name, scd_baseline[env_name], config_main, config_env, **env_opts)
            #log.debug("Generated config %s" % str(c))
            cfg_path = config_main.CFG_TEST_DIR + '/' + env_name + '.conf'
            util.save_config(cfg_path, c)
            #log.debug("Saving Config" % cfg_path)
#            log.debug("Config Test env_name %s" % c.env_name)
#            log.debug("Config Test artifactory %s" % c.artifactory)

    if args['report']:
        cfg_baseline, cfg_test = load_all_cfg(config_main, config_env)
        report.generate_report(cfg_baseline, cfg_test)
            
    if args['fake']:
        log.info("Building Fake SCD files")
        i = 0
        for env_name in config_env.ENV_LIST_ALL:
            fake_scd = build_scd.build_fake_scd(env_name, i)
            i = i + 2
            util.save_config(config_main.SCD_TEST_DIR + '/' + env_name + '/data.json', fake_scd)

    if args['promote']:
        log.info("Promoting Test files to baseline")
        for env_name in config_env.ENV_LIST_ALL:
            src_path = config_main.SCD_TEST_DIR + '/' + env_name + '/data.json'
            dest_path = config_main.SCD_BASELINE_DIR + '/' + env_name + '/data.json'
            log.debug("Copying file from %s to %s" % (src_path, dest_path))
            try:
                copyfile(src_path, dest_path)
            except:
                log.error("Failure promoting SCD files")

            src_path = config_main.CFG_TEST_DIR + '/' + env_name + '.conf'
            dest_path = config_main.CFG_BASELINE_DIR + '/' + env_name + '.conf'
            log.debug("Copying file from %s to %s" % (src_path, dest_path))
            try:
                copyfile(src_path, dest_path)
            except:
                log.error("Failure promoting SCD files")

        #log.info("Loading all Baseline and Test CFG Files")
        #cfg_baseline, cfg_test = load_all_cfg(config_main, config_env)
        #log.debug("Loaded CFG Baseline: %s" % str(cfg_baseline))
        #log.debug("Loaded CFG Test: %s" % str(cfg_test))

        

if __name__ == "__main__":

    main()
