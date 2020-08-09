from util import combineAttributes

APP1_DEFAULT_PORTS = { 'APP1_PORT1' : '7101',
		       'APP1_PORT2' : '7102',
		       'APP1_PORT3' : '7103'
		      }

APP2_DEFAULT_PORTS = { 'APP2_PORT1' : '8001',
		       'APP2_PORT2' : '8002',
		       'APP2_PORT3' : '8003'
		      }

APP3_DEFAULT_PORTS = { 'APP3_PORT1' : '9001',
		       'APP3_PORT2' : '9002',
		       'APP3_PORT3' : '9003'
		      }

ALL_DEFAULT_PORTS = combineAttributes(APP1_DEFAULT_PORTS, APP2_DEFAULT_PORTS, APP3_DEFAULT_PORTS)

