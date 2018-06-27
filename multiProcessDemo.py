#!/usr/bin/env python3

from multiprocessing import Process
import os
from time import sleep
import random

def info():
    print()

def f(name):
    print('%6d      \\_ %s (START)' % (os.getpid(),name))
    sleep(random.random())
    print('%6d      \\_ %s (END)' % (os.getpid(),name))

if __name__ == '__main__':
    print('%6d %s' % (os.getppid(),'python3'))
    print('%6d  \\_ %s' % (os.getpid(),'MAIN LINE'))
    procs = []
    
    for x in range(10):
        rnd = random.randrange(900) + 100
        p = Process(target=f, args=('bob_%d_%d' % (x,rnd),))
        p.start()
        procs.append(p)

    for pp in procs:
        pp.join()
