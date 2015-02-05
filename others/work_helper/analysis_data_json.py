import os

xx = os.path.join(os.path.dirname(__file__), "xx.json")
fr = open(xx)
_ids = fr.readline()
_outlet = fr.readline()
ids = list()
for l in _ids.split(", "):
    ids.append(l)
    
outlets = dict()
for l in _outlet.split(", "):
    _l = l.split("=")
#     print _l[0]
    outlets[_l[0]] = _l[1]
print outlets
for x in ids:
    print x, outlets.get(x)