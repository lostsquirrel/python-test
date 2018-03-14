# -*- encoding: utf-8 -*-
import sys

def process(args):
    if len(args)  < 4:
        print("Usage: template_processor.py data_properties_file template_file output_file")
        return

    data = parse_properties(args[1])
    template_file = args[2]
    output_file = args[3]
    content = read_template(template_file) % data
    write_output(output_file, content)


def read_template(template_file):
    fh = open(template_file)
    template = fh.read()
    fh.close()
    return template

def parse_properties(props):
    fh = open(props)
    data = dict()
    for l in fh:
        if not l.startswith("#") and len(l.strip()) > 0 :
            item = l.split("=")
            v = ''
            if len(item) > 1:
                v = item[1].strip()
            data[item[0].strip()] = v
    fh.close()
    print('read data from file %s' %  props)
    return data


def write_output(output_file, content):
    print("write content to file %s" % output_file)
    fh = open(output_file, 'w')
    fh.write(content)
    fh.flush()
    fh.close()


if __name__ == '__main__':
    args = sys.argv
    process(args)