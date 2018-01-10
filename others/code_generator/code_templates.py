# -*- coding: utf-8 -*-


alarm_template = '''
package net.cdsunrise.giraffe.domain;

import java.io.Serializable;
import java.util.Date;

/**
 * {{model_desc}}- 报警数据
 */
public class {{model_name}}Alarm implements Serializable {

    private Long id;
    /** 类型 */
    private {{model_name}}AlarmCategory alarmCategory;

    /** 故障状态 */
    private {{model_name}}FailureState failureState;

    /** 时间 */
    private Date alarmTime;

    /** 故障信息 */
    private String alarmDescription;

    /** 处理人 */
    private String handleUserId;

    /** 处理意见 */
    private String handleTreatment;

    public {{model_name}}AlarmCategory getAlarmCategory() {
        return alarmCategory;
    }

    public void setAlarmCategory({{model_name}}AlarmCategory alarmCategory) {
        this.alarmCategory = alarmCategory;
    }

    public {{model_name}}FailureState getFailureState() {
        return failureState;
    }

    public void setFailureState({{model_name}}FailureState failureState) {
        this.failureState = failureState;
    }

    public Date getAlarmTime() {
        return alarmTime;
    }

    public void setAlarmTime(Date alarmTime) {
        this.alarmTime = alarmTime;
    }

    public String getAlarmDescription() {
        return alarmDescription;
    }

    public void setAlarmDescription(String alarmDescription) {
        this.alarmDescription = alarmDescription;
    }

    public String getHandleUserId() {
        return handleUserId;
    }

    public void setHandleUserId(String handleUserId) {
        this.handleUserId = handleUserId;
    }

    public String getHandleTreatment() {
        return handleTreatment;
    }

    public void setHandleTreatment(String handleTreatment) {
        this.handleTreatment = handleTreatment;
    }
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }
}
'''

alarm_category_template = '''
package net.cdsunrise.giraffe.domain;

public class {{model_name}}AlarmCategory extends Category {

}
'''

failure_state_template = '''
package net.cdsunrise.giraffe.domain;

import java.io.Serializable;

public class {{model_name}}FailureState extends FailureState implements Serializable {

}
'''

realtime_template = '''
package net.cdsunrise.giraffe.domain;

import java.io.Serializable;

/**
 * {{model_desc}}- 实时数据
 */
public class {{model_name}}Realtime implements Serializable {

 private Long id;

    /** 运行状态  */
    private int runningState;

    /** 通信状态 */
    private int communicationState;

    /** 手自动开关状态（手动/自动） */
    private int switchModel;

    /** 故障报警 */
    private String failureAlarm;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getRunningState() {
        return runningState;
    }

    public void setRunningState(int runningState) {
        this.runningState = runningState;
    }

    public int getCommunicationState() {
        return communicationState;
    }

    public void setCommunicationState(int communicationState) {
        this.communicationState = communicationState;
    }

    public int getSwitchModel() {
        return switchModel;
    }

    public void setSwitchModel(int switchModel) {
        this.switchModel = switchModel;
    }

    public String getFailureAlarm() {
        return failureAlarm;
    }

    public void setFailureAlarm(String failureAlarm) {
        this.failureAlarm = failureAlarm;
    }
}

'''

service_template = '''
package net.cdsunrise.giraffe.service;

import net.cdsunrise.giraffe.domain.{{model_name}}Alarm;
import net.cdsunrise.giraffe.domain.{{model_name}}Realtime;

public interface {{model_name}}MonitorService {

    /**
     * @param id 编号
     * @return
     */
    {{model_name}}Realtime getRealtime(Long id);


    /**
     * @return
     */
    {{model_name}}Alarm getAlarm(Long id);
}

'''

controller_template = '''
package net.cdsunrise.giraffe.controller;

import net.cdsunrise.giraffe.domain.{{model_name}}Alarm;
import net.cdsunrise.giraffe.domain.{{model_name}}Realtime;
import net.cdsunrise.giraffe.service.{{model_name}}MonitorService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * {{model_desc}}
 */
@RestController
@RequestMapping("/{{model_path}}")
public class {{model_name}}MonitorController {

    private {{model_name}}MonitorService cacMonitorService;

    public {{model_name}}MonitorController({{model_name}}MonitorService cacMonitorService) {
        this.cacMonitorService = cacMonitorService;
    }

    /**
     * 实时数据
     * @return
     */
    @GetMapping("/realtime/{id}")
    public {{model_name}}Realtime realtime(@PathVariable("id")Long id) {
        {{model_name}}Realtime realtime = cacMonitorService.getRealtime(id);
        return realtime;
    }

    /**
     * 报警数据
     * @return
     */
    @RequestMapping("/alarm/{id}")
    public {{model_name}}Alarm alarm(@PathVariable("id")Long id) {
        return cacMonitorService.getAlarm(id);
    }

}

'''

service_mock_template = '''
@Bean
@ConditionalOnMissingBean
public {{model_name}}MonitorService {{model_name_lower}}MonitorService() {
    return new {{model_name}}MonitorService() {
        @Override
        public {{model_name}}Realtime getRealtime(Long id) {
            {{model_name}}Realtime rt = ({{model_name}}Realtime) MockConfig.this.mockRandomBean.createMockRandomBean({{model_name}}Realtime.class);
            rt.setId(id);
            return rt;
        }
        @Override
        public {{model_name}}Alarm getAlarm(Long id) {
            {{model_name}}Alarm alarm = ({{model_name}}Alarm) MockConfig.this.mockRandomBean.createMockRandomBean({{model_name}}Alarm.class);
            alarm.setId(id);
            return alarm;
        }
    };
}
'''


templates = dict(
    service_mock=service_mock_template,
    service=service_template,
    controller=controller_template,
    realtime=realtime_template,
    failure_state=failure_state_template,
    alarm_category=alarm_category_template,
    alarm=alarm_template
)


def get_template(name):
    return templates[name]