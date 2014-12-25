'''
Created on Oct 9, 2014

@author: lisong
'''
def clean_script(sf, bf):
    
#     source = open(sf, "r+")
#     backup = open(bf, "w")
#     backup.write(source.read())
#     backup.close()
#     source.close()
    
    s = open(sf, "r")
    t = open(bf, "w")
    line_number = 0
    start_line = 0
    end_line = 0
    keep_content = True
    new_content = ""
    for line in s:
        line_number += 1
        if "<script" in line:
    #         print 'script start'
            start_line = line_number
            keep_content = False
        if "</script>" in line:
    #         print 'script end'
            end_line = line_number
            keep_content = True
            continue
        if start_line > 0:
            if start_line != end_line and keep_content:
                new_content += line
        else :
            new_content += line
             
    t.write(new_content)
    s.close()
    t.close()
    
sf = "/home/lisong/KuaiPan/Dropbox/ref/www.vogella.com/tutorials/ComplexityAnalysis/article.html"
bf = "/home/lisong/KuaiPan/Dropbox/ref/www.vogella.com/algorithms/ComplexityAnalysis.html"
clean_script(sf, bf)