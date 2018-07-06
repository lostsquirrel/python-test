#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aliyunsdkalidns.request.v20150109 import DescribeDomainInfoRequest, DescribeDomainRecordsRequest, UpdateBatchDomainRecordsRequest, UpdateDomainRecordRequest
from aliyunsdkcore.client import AcsClient
config_file = "ali_access_key.conf"
# ak = ''
# secret = ''

def get_access():
    fh = open(config_file)
    cfgs = fh.readlines()
    return cfgs[0].strip(), cfgs[1].strip()


def get_client():
    ak, secret = get_access()
    return AcsClient(
        ak,
        secret,
    )


# def query_list():
#     qdl = QueryDomainListRequest.QueryDomainListRequest()
#     qdl.set_PageNum(1)
#     qdl.set_PageSize(10)
#     # qdl.get_DomainName()
#     # print(get_client().get_access_key())
#     res = get_client().do_action_with_exception(qdl)
#     print(res)


def domain_info(domain):
    qdd = DescribeDomainInfoRequest.DescribeDomainInfoRequest()
    qdd.set_DomainName(domain)
    res = get_client().do_action_with_exception(qdd)
    print(res)


def domain_records(domain):
    ddr = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    ddr.set_DomainName(domain)
    ddr.set_PageNumber(1)
    ddr.set_PageSize(10)
    res = get_client().do_action_with_exception(ddr)
    print(res)


def update_records(records):
    param = UpdateBatchDomainRecordsRequest.UpdateBatchDomainRecordsRequest()

    param.set_Records(records)
    res = get_client().do_action_with_exception(param)
    print(res)


def update_record():
    param = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    param.set_RecordId("3831937780651008")
    param.set_Value("123")
    param.set_RR("_acme-challenge")
    param.set_Type("TXT")
    res = get_client().do_action_with_exception(param)
    print(res)


if __name__ == '__main__':
    domain = "shangao.tech"
    update_record()
    # records = [{
    #   "RecordId": "3831937780651008",
    #   # "RR": "_acme-challenge",
    #   #
    #   "Value": "123",
    #   # "Type": "TXT",
    #   # "DomainName": "shangao.tech",
    #   # "Line": "default",
    #   # "TTL": 600
    # }, {
    #   # "RR": "_acme-challenge",
    #   "RecordId": "3831937769378816",
    #   "Value": "456",
    #   # "Type": "TXT",
    #   # "DomainName": "shangao.tech",
    #   # "Line": "google",
    #   # "TTL": 600
    # }]
    # update_records(records)
