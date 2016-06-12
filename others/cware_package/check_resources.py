# encoding: utf-8
import os

def read_tree(tree_path, tree_home):
    fh = open(tree_path)
    content = ''
    for l in fh:
        l = l.decode('gbk')
        # content += l
        if l.find('addtree') != -1:
            _l = l.split(',')
            if len(_l) == 3:
                res = _l[1].strip()[1:-1]
                # print res
                res_path = '%s\\%s' % (tree_home, res)
                if not os.path.exists(res_path):
                    print res_path
if __name__ == '__main__':
    package_target = 'F:\\package_target_v3'
    for x in os.listdir(package_target):
        # x = x.decode('gbk')
        tree_home = '%s\\%s' % (package_target, x.decode('gbk'))
        tree1 = '%s\\TreeTest01.htm' % tree_home
        if not os.path.exists(tree1.encode('gbk')):
            print 'Tree not exist in %s' % x.decode('gbk')
            continue
        read_tree(tree1, tree_home)
        tree2 = '%s\\TreeTest02.htm' % tree_home
        if not os.path.exists(tree2.encode('gbk')):
            print 'Tree not exist in %s' % x.decode('gbk')
            continue
        read_tree(tree2, tree_home)
