fh = open('index.source')
content = ''
for line in fh:
    try :
        if line.endswith('\n'):
            line = line[:-1]
        x = line.split('.')
    #         print x
        if x[1] in ('html', 'xml'):
            content += '\t\t\t<li><a href="%s">%s</a></li>\n' % (line, x[0])
    except IndexError:
        print 'skip this line', line
    
print content