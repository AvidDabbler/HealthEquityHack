import queue
from threading import Thread
import pandas as pd
import math

MAX_THREAD = 100


class Batch_Job:
    def __init__(self,func,args,dataset):
        self.func = func
        self.args = args
        self.dataset = dataset
        self.q = queue.Queue()
        self.thread_list = list()


    def run(self):
        if len(self.dataset) <= MAX_THREAD:
            for i in range(len(self.dataset)):
                self.func(self.args,self.dataset.iloc[[i]])

        else:
            iter = int(len(self.dataset)/MAX_THREAD)
            step = 0
            while step <= len(self.dataset):


                step += iter

                if step >= len(self.dataset):

                    thread = Thread(target=lambda q, arg1, dframe,start: q.put(self.func(arg1, dframe,start )),
                                                   args=(self.q, self.args, self.dataset.iloc[step - iter:len(self.dataset)],(step - iter)))
                    self.thread_list.append(thread)
                    thread.start()
                    break
                thread = Thread(target=lambda q, arg1, dframe,start: q.put(self.func(arg1, dframe,start)),
                                args=(self.q, self.args, self.dataset.iloc[step - iter:step-1],(step - iter)))


                self.thread_list.append(thread)
                thread.start()







    def join_threads(self):
        for t in self.thread_list:
            t.join()
        frame_list = list()
        while not self.q.empty():
            frame_list.append(self.q.get())
        return pd.concat(frame_list)



