from util import combineAttributes
from Config import AttributeDict

ENV_TYPE_KEY = 'env_type'
ENV_TYPE_DEV_VALUE = 'dev'
ENV_TYPE_TEST_VALUE = 'tst'
ENV_TYPE_OPS_VALUE = 'ops'

FEATURE1_KEY = 'feature1_flag'
FEATURE2_KEY = 'feature2_flag'

CLOUD_FLAG_KEY = 'cloud_flag'
SMALL_FLAG_KEY = 'small_flag'

DEV_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_DEV_VALUE }
TST_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_TEST_VALUE }
OPS_ENV_TYPE_OPTS = { ENV_TYPE_KEY : ENV_TYPE_OPS_VALUE  }

DEFAULT_ENV_TYPE_OPT = DEV_ENV_TYPE_OPTS
DEFAULT_CLOUD_FLAG_OPT = { CLOUD_FLAG_KEY : False }
DEFAULT_SMALL_FLAG_OPT = { SMALL_FLAG_KEY : False }
DEFAULT_FEATURES_OPTS = {   FEATURE1_KEY : False,
	                    FEATURE2_KEY : False  }

ALL_DEFAULT_OPTS = combineAttributes(DEFAULT_ENV_TYPE_OPT, DEFAULT_CLOUD_FLAG_OPT, DEFAULT_SMALL_FLAG_OPT, DEFAULT_FEATURES_OPTS)

all_features_on = {   FEATURE1_KEY : True,
                      FEATURE2_KEY : True  }

small_env = { SMALL_FLAG_KEY : True }
small_cloud_env = { SMALL_FLAG_KEY : True,
                    CLOUD_FLAG_KEY : True
                  }

CONFIG1_OPTS = combineAttributes(ALL_DEFAULT_OPTS, all_features_on)
CONFIG2_OPTS = combineAttributes(ALL_DEFAULT_OPTS, small_env)
CONFIG3_OPTS = combineAttributes(ALL_DEFAULT_OPTS, small_cloud_env)

ENV_LIST_ALL = AttributeDict()
ENV_LIST_ALL['Env1'] = ALL_DEFAULT_OPTS
ENV_LIST_ALL['Env2'] = ALL_DEFAULT_OPTS
ENV_LIST_ALL['Env3'] = ALL_DEFAULT_OPTS
ENV_LIST_ALL['Env4'] = ALL_DEFAULT_OPTS
ENV_LIST_ALL['Env5'] = ALL_DEFAULT_OPTS
ENV_LIST_ALL['Env6'] = ALL_DEFAULT_OPTS
