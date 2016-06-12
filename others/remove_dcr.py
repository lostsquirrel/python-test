import os

base_path = u'F:\\package_target_v21\\'
for x in os.listdir(base_path):
    print x
    tree1 = u'%s\\%s\\TreeTest01.htm' % (base_path, x)
    print os.path.exists(tree1)
    fh = open(tree1)
    for l in fh:
        print l