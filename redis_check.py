# -*- coding: utf-8 -*-
import time

import requests

if __name__ == '__main__':

    while True:
        fh = requests.get("http://192.168.10.216:18325/redis")
        content = fh.json()
        fee = content['feeIslandData']
        # print(fee)
        data = list(filter(lambda x: x["name"].endswith("DayData"), fee))
        data_ = list(filter(lambda x: x["name"] in ('L_DayData', "R_DayData", 'LR_DayData'), data))
        for d in data_:
            print('{name}: {value} {timeString}'.format(**d))
        time.sleep(10)
    # print(list(data))