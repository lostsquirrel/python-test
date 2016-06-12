from my_config import dbname as bdb;
import my_config
def setDb(dbname = "bdb"):
    print "dbname from config is %s" % my_config.dbname
    my_config.dbname = dbname
    print "dbname has been set to %s in b" % dbname

print 'pring dbname in b %s' % bdb