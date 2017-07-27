# -*- coding: utf-8 -*-

import time
def echo(i):
    time.sleep(0.001)
    return i

# Non Deterministic Process Pool
from multiprocessing.pool import Pool as mPool
"""""
python:multiprocessing 在windows中的使用：
RuntimeError: 
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.
This probably means that you are not using fork to start your

        child processes and you have forgotten to use the proper idiom
        in the main module:
multiprocessing的使用在Linux和mac中直接使用即可，但是在window中不太一样

python-2.7-docs-html/library/multiprocessing.html#multiprocessing-programming
简而言之，需要在p=Process()前加上 
if __name__ == ‘__main__’:
      p = Process(...
Safe importing of main module
    Make sure that the main module can be safely imported by a new Python interpreter without causing unintended side effects (such a starting a new process).
    For example, under Windows running the following module would fail with a RuntimeError:
    from multiprocessing import Process
    def foo():
        print 'hello'
    p = Process(target=foo)
    p.start()
    Instead one should protect the “entry point” of the program by using if __name__ == '__main__': as follows:
    from multiprocessing import Process, freeze_support
    def foo():
        print 'hello'
    if __name__ == '__main__':
        freeze_support()
        p = Process(target=foo)
        p.start()
    (The freeze_support() line can be omitted if the program will be run normally instead of frozen.)
    This allows the newly spawned Python interpreter to safely import the module and then run the module’s foo() function.
"""""
'''''
if __name__ == '__main__':      # windows
    p = mPool(10)
    run1 = [a for a in p.imap_unordered(echo,list(range(10)))]
    run2 = [a for a in p.imap_unordered(echo,list(range(10)))]
    run3 = [a for a in p.imap_unordered(echo,list(range(10)))]
    run4 = [a for a in p.imap_unordered(echo,list(range(10)))]
    print(run1 == run2 == run3 ==run4)
'''''
# Deterministic Gevent Pool
from gevent.pool import Pool as gPool
p = gPool(10)
run1 = [a for a in p.imap_unordered(echo,list(range(10)))]
run2 = [a for a in p.imap_unordered(echo,list(range(10)))]
run3 = [a for a in p.imap_unordered(echo,list(range(10)))]
run4 = [a for a in p.imap_unordered(echo,list(range(10)))]
print(run1 == run2 == run3 ==run4)
