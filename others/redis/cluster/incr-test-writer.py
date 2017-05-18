from redis._compat import xrange
from others.redis.cluster import rc
from others.redis.cluster import current_milli_time

s = current_milli_time()
for i in xrange(1000000):
    d = str(i)
    rc.set(d, d)
    rc.incrby(d, 1)

print current_milli_time() - s


# 1824127
# 1482678 32 conn