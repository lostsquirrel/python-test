# encoding: utf-8
import os
from tree_template import study_template
from tree_template import practise_template
from base import package_target
from tree_parser import parse_tree


def list_xmls(xpath, res_context):
    xmls = os.listdir(xpath)
    ptag = False
    for xml_file in xmls:
        # xml_file = unicode(xml_file.decode('gb2312').encode('utf-8'))
        # print type(xml_file)
        if xml_file.endswith('xue.xml'):
            # print '%s\\%s' % (xpath, xml_file)
            write_to_study(res_context, name, '%s\\%s' % (xpath, xml_file))
            ptag = True
        elif xml_file.endswith('lian.xml'):
            # print '%s\\%s' % (xpath, xml_file)
            write_to_practise(res_context, name, '%s\\%s' % (xpath, xml_file))
            ptag = True
    if not ptag:
        print 'Error Process: ' + name
    # print xmls


def write_to_study(res_context, name, xml_file):
    study_path = '%s\\%s\\TreeTest01.htm' % (package_target, name)
    item_path = '%s\\%s\\' % (package_target, name)
    content = study_template % parse_tree(item_path, res_context, xml_file)

    write_tree(study_path, content)

def write_to_practise(res_context, name, xml_file):
    practise_path = 'F:\\package_target\\%s\\TreeTest02.htm' % name
    content = practise_template % parse_tree(res_context, xml_file)
    write_tree(practise_path, content)


def write_tree(tree_path, content):
    h = open(tree_path, 'w')
    h.write(content.encode('gb2312'))
    h.close()