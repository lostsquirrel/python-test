from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import time

s = time.time()
print sqlalchemy.__version__

notify_connection_url = 'postgresql://postgres:sale114@db0.soulagou.com:5433/soulagou_notify'

notify_engine = create_engine(notify_connection_url, echo=False, pool=None)
NotifySession = sessionmaker(bind=notify_engine)
#sqlalchemy.orm.session.Session#
xx = NotifySession()

sql = 'select * from message'
rp = xx.execute(sql, dict(xid=58))
# rs = rp.fetchall()
# print rs
print rp.fetchone()
xx.close()

print time.time() - s