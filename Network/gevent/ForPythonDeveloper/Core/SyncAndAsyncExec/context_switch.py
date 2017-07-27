# -*- coding: utf-8 -*-
__author__ = 'chzfmx'

'''''
上下文切换
在gevent里面，上下文切换是通过yielding来完成的. 在下面的例子里， 我们有两个上下文，通过
调用gevent.sleep(0)，它们各自yield向对方
'''''
import gevent
def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context switch to bar')
    gevent.sleep(0)
    print('Implicit context switch to bar')

gevent.joinall([gevent.spawn(foo),gevent.spawn(bar)])




