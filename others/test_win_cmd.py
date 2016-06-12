import os


def copy_base(name):
    dest = os.path.join("F:\\", 'package_target\\%s\\' % name)
    # shutil.copy("F:\\package_base\\", dest)
    os.system("xcopy %s %s /S /E /Y" % ("F:\\package_base\\*", dest))

def copy_base_index(name):
    dest = os.path.join("F:\\", 'package_target\\%s\\' % name)
    # shutil.copy("F:\\package_base\\", dest)
    os.system("xcopy %s %s /S /E /Y" % ("F:\\package_base\\index.htm", dest))








def copy_clut3d(res_home, name):
    try:
        os.system('mkdir F:\\package_target\\%s\\images_cult3d' % name)
    except Exception, e:
        print e
    os.system('xcopy %s\\images_cult3d F:\\package_target\\%s\\images_cult3d  /S /E /Y' % (res_home, name))

def copy_pic(res_home, name):
    os.system('xcopy %s\\Theme\\pic F:\\package_target\\%s\\pic  /S /E /Y' % (res_home, name))

def find_c(ccpath):
    ccc = os.listdir(ccpath)
    for x in ccc:
        nextcc = '%s\\%s' % (ccpath, x)
        if os.path.isdir(nextcc):
            find_c(nextcc)
        else:
            if x.startswith('c') and (x.endswith('.co') or x.endswith('.swf') or x.endswith('.dcr')):
                print 'del %s' % nextcc
                os.system('del %s' % nextcc)
if __name__ == '__main__':
    pass
    copy_base_js()
    # find_c('F:\\package_target\\')
    # tag = False
    # for name in os.listdir(package_source):
    #     os.system('rd F:\\package_target\\%s\\tmp /q' % name)
        # if name == 'TRSS0000014':
        #     tag = True
        #
        # ccpath = "%s\\%s" % (package_source, name)
        # ras = ResourcesAnalysis()
        # ras.find_resources(ccpath)
        # rps = ras.get_path()
        # res_home = rps[0]
        # res_home = res_home[:res_home.rfind('\\')]
        # copy_clut3d(res_home, name)
        # copy_pic(res_home, name)
        # print res_home
        # res_context = res_home[res_home.find(template) + len(template):].replace('\\', '/')
        # print name
        # if tag:
        #     print res_context
        #     list_xmls(rps[1], res_context)
            # os.system('del F:\\package_target\\%s\\*.js' % name)
            # os.system('del F:\\package_target\\%s\\about.htm' % name)
            # os.system("mkdir F:\package_target\\%s\\resource" % name)
            # xcp = "xcopy %s F:\\package_target\\%s\\resource\\ /s " % (sp, name)
            # print xcp
            # os.system(xcp)
            # dest = os.path.join("F:\\", 'package_target\\%s\\resource\\' % name)
            # print dest
            # shutil.copytree(sp, dest)
            # copy_base(name)
            # copy_base_js(name)