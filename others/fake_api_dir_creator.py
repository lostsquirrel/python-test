import json
import os

data = json.load(open('C:/Users/lisong/Documents/_sunrise-wuhu.postman_collection.json'));
# TODO request add content into files
root_path = 'data'
for model in data['item']:
    model_name = model['name']
    print model_name
    model_path = r'%s\%s' % (root_path, model_name)
    for req in model['item']:
        req_url = req['request']['url']['raw']
        print req_url
        req_dir = req_url[req_url.index("}}/") + 3:req_url.rindex('/')]
        req_dir = req_dir.replace("/", "\\")
        req_path = r"%s\%s" % (model_path, req_dir)
        print req_path
        file_name = req_url[req_url.rindex('/')+1:]
        if "?" in file_name and file_name.index("?") > 0:
            file_name = file_name[:file_name.index("?")]
        print file_name
        os.system('echo.>%s\%s' % (req_path, file_name))