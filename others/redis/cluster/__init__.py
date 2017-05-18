from rediscluster import StrictRedisCluster
import time

current_milli_time = lambda: int(round(time.time() * 1000))
startup_nodes = [{"host": "192.168.1.139", "port": "7000"}]

# Note: decode_responses must be set to True when used with python3
rc = StrictRedisCluster(startup_nodes=startup_nodes,  max_connections=32, decode_responses=True)