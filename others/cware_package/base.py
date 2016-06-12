# encoding: utf-8
import os

package_source = 'F:\\package_source'
package_target = 'F:\\package_target_v21'
template = 'template'
resources = 'resources'
resource = 'resource'
xmls = ['XML_1.0', 'XML_V1.0']


class ResourcesAnalysis(object):
    def __init__(self):
        self.res_path = None
        self.xml_path = None

    def find_resources(self, ccpath):
        ccc = os.listdir(ccpath)
        for x in ccc:
            nextcc = '%s\\%s' % (ccpath, x)
            if os.path.isdir(nextcc):
                # print x
                if x in xmls and self.xml_path is None:
                    self.xml_path = nextcc
                if resources == x and self.res_path is None:
                    self.res_path = nextcc[:-len(resources) - 1]
                elif resource == x and self.res_path is None:
                    self.res_path = nextcc[:-len(resource) - 1]

                if self.res_path is None:
                    self.find_resources(nextcc)

    def get_path(self):
        return self.res_path, self.xml_path