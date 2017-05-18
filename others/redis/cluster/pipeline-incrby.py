from redis._compat import xrange
from others.redis.cluster import rc
from others.redis.cluster import current_milli_time

s = current_milli_time()
for i in xrange(1000000):
    d = str(i)
    pipe = rc.pipeline(transaction=False)
    pipe.set(d, d)
    pipe.incrby(d, 1)
    pipe.execute()

    pipe = rc.pipeline(transaction=False)
    pipe.set("foo-{0}".format(d), d)
    pipe.incrby("foo-{0}".format(d), 1)
    pipe.set("bar-{0}".format(d), d)
    pipe.incrby("bar-{0}".format(d), 1)
    pipe.set("bazz-{0}".format(d), d)
    pipe.incrby("bazz-{0}".format(d), 1)
    pipe.execute()

print current_milli_time() - s

# 2166761