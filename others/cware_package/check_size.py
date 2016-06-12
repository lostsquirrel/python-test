import os
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

package_target = 'F:\\package_target_v3'
for x in os.listdir(package_target):
    p = os.path.join(package_target, x)
    print x.decode('gbk'), get_size(p) / 1024 /1024