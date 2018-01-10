# -*- coding: utf-8 -*-
from tornado import template
from code_templates import get_template
from code_templates import templates

out_dirs = dict(
    service_mock=None,
    service=r"%s\service\%sMonitorService.java",
    controller=r"%s\controller\%sMonitorController.java",
    realtime=r"%s\domain\%sRealtime.java",
    failure_state=r"%s\domain\%sFailureState.java",
    alarm_category=r"%s\domain\%sAlarmCategory.java",
    alarm=r"%s\domain\%sAlarm.java"
)


def generator(model, meta):
    t = template.Template(get_template(meta['template_name']))
    content = t.generate(**model)
    if meta['out'] is None:
        print(content)
    else:
        fh = open(meta['out'], 'w')
        fh.write(content)
        fh.close()


def monitor_generator():
    name = "CCTV"
    mp = 'cctv'
    md = '视频系统监控'
    nl=name[:1].lower() + name[1:]
    model = dict(model_name=name, model_desc=md, model_path=mp, model_name_lower=nl)
    base_path = r'E:\Works\wuhu_monitor\monitor\src\main\java\net\cdsunrise\giraffe'
    for k, v in templates.iteritems():
        k_ = out_dirs[k]
        mo = None
        if k_ is not None:
            mo = k_ % (base_path, name)
        meta = dict(template_name=k, out=mo)
        print(meta)
        generator(model, meta)


if '__main__' == __name__:
    monitor_generator()
