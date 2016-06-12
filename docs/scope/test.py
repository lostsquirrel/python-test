import my_config
from a import setDb as setDbByA
from b import setDb as setDbByB
if __name__ == '__main__':
    print 'current dbname is %s' % my_config.dbname
    setDbByA()
    print 'after a set dbname is %s' % my_config.dbname
    setDbByB()
    print 'after b set dbname is %s' % my_config.dbname
