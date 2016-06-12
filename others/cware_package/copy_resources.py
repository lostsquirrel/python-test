# encoding: utf-8
import os

def copy_base_js():
    for name in os.listdir('F:\\package_target_v21\\'):
        dest =  'F:\\package_target_v2\\%s\\js' % name.decode('gbk')
        del_cmd = 'del %s\\* /s/q' % dest
        print del_cmd
        os.system(del_cmd.encode('gbk'))
        cp_cmd = "xcopy %s %s /S /E /Y" % ("F:\\package_base\\js", dest)
        print cp_cmd
        os.system(cp_cmd.encode('gbk'))


def copy_base_treejs():
    package_target = 'Z:\\开发部\\李嵩\\package_target_v3'.decode('utf-8')
    package_target = 'F:\\package_target_v3'
    print type(package_target)
    # print package_target.decode('utf-8')
    for name in os.listdir(package_target.encode('gbk')):
        dest = '%s\\%s\\MENUTREE\\MENUTREE.JS' % (package_target, name.decode('gbk'))
        del_cmd = 'del %s' % dest
        print del_cmd
        os.system(del_cmd.encode('gbk'))
        cp_cmd = "copy %s %s /Y" % ("F:\\package_base\\MENUTREE\\MENUTREE.JS", dest)
        print(cp_cmd)
        os.system(cp_cmd.encode('gbk'))

def copy_base_css():
    for name in os.listdir('F:\\package_target_v21\\'):
        dest =  'F:\\package_target_v21\\%s\\css\\tree.css' % name.decode('gbk')
        del_cmd = 'del %s' % dest
        print del_cmd
        os.system(del_cmd.encode('gbk'))
        cp_cmd = "copy %s %s /Y" % ("F:\\package_base\\css\\tree.css", dest)
        print(cp_cmd)
        os.system(cp_cmd.encode('gbk'))

if __name__ == '__main__':
    copy_base_treejs()