import os

def get_cware_list():
    fh = open('course_list.txt')
    cs = dict()
    for l in fh:
        _l = l.split('\t')
        cs[_l[0].strip()] = _l[3].strip()
    fh.close()

    return cs

if __name__ == '__main__':
    pass
    cs = get_cware_list()
    # for x in os.listdir('F:\\package_target\\'):
    #     # print x
    #     x_ = 'F:\\package_target\\%s' % x
    #     # x_ = x_.decode('utf-8')
    #     # print x_
    #     # print type(x_)
    #     # print 'Exist: %s' % str(os.path.exists(x_))
    #     if os.path.exists(x_) and (cs.get(x) is not None):
    #         # cmd = u'xcopy F:\\package_target\\%s %s  /S /E /Y' % (x, x_)
    #         cmd = u'ren F:\\package_target\\%s %s' % (x, cs[x].decode('utf-8'))
    #         print cmd
    #         cmd = cmd.encode('utf-8')
    #         # print type(cmd)
    #         #
    #         os.system(cmd)

    for x in os.listdir('F:\\package_target\\'):

        if not x.startswith('__'):
            # print x
            try:
                x2 = x.decode('gb18030')
                # print x2
                # print os.path.exists(u'F:\\package_target\\' + x2)
                print u'ren F:\\package_target\\%s %s'% (x2, x.decode('utf-8'))
            except UnicodeDecodeError, e:
                pass
            # x3 = x.decode('utf-8')
            # print x3
            # print os.path.exists(u'F:\\package_target\\' + x3)
            # x4 = x.decode('utf-8').encode('gbk')
            # print x4
            # print os.path.exists('F:\\package_target\\' + x4)
            # print type(x)

            # x_ = u'F:\\package_target\\' + x2
            # if os.path.exists(x_):
            #     try:
            #         cmd = u'ren ' + x_ + u' ' + x.decode('utf-8')
            #         # print type(cmd)
            #         #
            #         # print cmd
            #     except UnicodeDecodeError, e:
            #         print 'cmd: ' + str(e)