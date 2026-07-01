import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hoangkn/Hoang/Main-Projects/SentinelDrone/bookros2_ws/install/launch_pal'
