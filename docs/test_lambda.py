def make_incrementor(n):
    return lambda x: x + n

# f = make_incrementor(42)
# print make_incrementor(0)
# 
# print make_incrementor(1)(2)

def xx(e):
    return e[1]
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
print pairs
pairs.sort(key=xx)
print pairs