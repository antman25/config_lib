from env_info import EnvInfo
from util import combineOptions

ENV_TYPE_KEY = 'env_type'
ENV_TYPE_DEV_VALUE = 'dev'
ENV_TYPE_TEST_VALUE = 'tst'
ENV_TYPE_OPS_VALUE = 'ops'


DEV_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_DEV_VALUE }
TST_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_TEST_VALUE }
OPS_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_OPS_VALUE  }

DEFAULT_ENV_TYPE_OPT = DEV_ENV_TYPE_OPTS

CLOUD_FLAG_KEY = 'cloud_flag'

DEFAULT_CLOUD_FLAG_OPT = { CLOUD_FLAG_KEY : False }

SMALL_FLAG_KEY = 'small_flag'
DEFAULT_SMALL_FLAG_OPT = { SMALL_FLAG_KEY : False }

FEATURE1_KEY = 'feature1_flag'
FEATURE2_KEY = 'feature2_flag'

DEFAULT_FEATURES_OPTS = {   FEATURE1_KEY : False,
	                    FEATURE2_KEY : False  }

ALL_DEFAULT_OPTS = combineOptions(DEFAULT_ENV_TYPE_OPT, DEFAULT_CLOUD_FLAG_OPT, DEFAULT_SMALL_FLAG_OPT, DEFAULT_FEATURES_OPTS)

all_features_on = {   FEATURE1_KEY : True,
                      FEATURE2_KEY : True  }

small_env = { SMALL_FLAG_KEY : True }
small_cloud_env = { SMALL_FLAG_KEY : True,
		            CLOUD_FLAG_KEY : True
    		  }

CONFIG1_OPTS = combineOptions(ALL_DEFAULT_OPTS, all_features_on)
CONFIG2_OPTS = combineOptions(ALL_DEFAULT_OPTS, small_env)
CONFIG3_OPTS = combineOptions(ALL_DEFAULT_OPTS, small_cloud_env)

ENV_LIST_A = [  EnvInfo(env_name='Env1', **ALL_DEFAULT_OPTS),
                EnvInfo(env_name='Env2', **combineOptions(ALL_DEFAULT_OPTS, TST_ENV_TYPE_OPTS)),
                EnvInfo(env_name='Env4', **combineOptions(CONFIG1_OPTS, TST_ENV_TYPE_OPTS))
            ]

ENV_LIST_B = [ EnvInfo(env_name='Env3', **combineOptions(ALL_DEFAULT_OPTS, OPS_ENV_TYPE_OPTS)) ]

ENV_LIST_C = [ EnvInfo(env_name='Env5', **combineOptions(CONFIG2_OPTS, TST_ENV_TYPE_OPTS)),
               EnvInfo(env_name='Env6', **combineOptions(CONFIG3_OPTS, DEV_ENV_TYPE_OPTS)) ] 

ENV_LIST_ALL = ENV_LIST_A + ENV_LIST_B + ENV_LIST_C
