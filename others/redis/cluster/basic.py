from others.redis.cluster import rc

rc.set("foo", "bar")

print(rc.get("foo"))