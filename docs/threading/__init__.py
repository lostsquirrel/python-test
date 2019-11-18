# -*- coding: utf-8 -*-
import threading
import time


class ThreadA(threading.Thread):

    def __init__(self, name: str, e: threading.Event):
        super().__init__(name=name)
        self.event = e

    def run(self):
        while self.event.is_set():
            print("{} {}".format(self.name, time.time()))
            time.sleep(1)
        else:
            print("event {}".format(self.event.is_set()))