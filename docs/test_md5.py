import hashlib

def hash_md5(source):
    m = hashlib.md5()
    m.update(source)
    return m.hexdigest();

for x in ['luyou123', 'test', '123456', '12345678']:
    msg = '%s: %s' % (x, hash_md5(x))
    print(msg)