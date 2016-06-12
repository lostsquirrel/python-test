from my_config import dbname as adb;
import my_config
def setDb(dbname = "adb"):
    print "dbname from config is %s" % my_config.dbname
    my_config.dbname = dbname
    print "dbname has been set to %s in a" % dbname

