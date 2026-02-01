import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/chrisjan/Documents/SpaceConcordia/IntroTask/install/py_task'
