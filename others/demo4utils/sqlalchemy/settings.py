__author__ = 'lisong'

import os

database_connection_url = 'sqlite:///%s/job.db' % os.path.join(os.path.dirname(__file__), "database")
