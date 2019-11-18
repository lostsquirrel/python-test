# -*- coding: utf-8 -*-
import threading
import time

from docs.threading import ThreadA

if __name__ == '__main__':
    e = threading.Event()
    e.set()
    print("set event to {}".format(e.is_set()))
    for x in range(10):
        s = ThreadA("Thread {}".format(x), e)
        s.start()

    time.sleep(10)
    e.clear()
    print("set event to {}".format(e.is_set()))
