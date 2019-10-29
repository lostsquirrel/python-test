# coding=utf-8
import json
from datetime import datetime, date
from decimal import Decimal

topic = 'my-topic'
group_id = 'my-group'
bootstrap_servers = ['localhost:9092']


class JSONEncoder(json.JSONEncoder):
    """Json 编码器"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


kafka_message_encoding = 'utf-8'