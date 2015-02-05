import json

a = dict(abc=123)
print a
content = json.dumps(a)
xx = json.loads(content)
print type(xx)