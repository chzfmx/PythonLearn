# -*- coding: utf-8 -*-

"""""
下面例子中的select()函数通常是一个在各种文件描述符上轮询的阻塞调用
"""""
'''''
import time
import gevent
from  gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)
def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('gr1 Start Polling: %s' % tic())
    select.select([],[],[],2)
    print('gr1 Ended Polling: %s' % tic())

def gr2():
    # Busy waits for s second, but we don't want to stick around...
    print('gr2 Start Polling: %s' % tic())
    select.select([],[],[],2)
    print('gr2 End Polling: %s' % tic())

def gr3():
    print('gr3 Hey Lets do some stuff while the greenlets poll, %s' % tic())
    gevent.sleep(1)

gevent.joinall([gevent.spawn(gr1),gevent.spawn(gr2),gevent.spawn(gr3)])
'''''



"""""
下面是另外一个多少有点人造色彩的例子，定义一个非确定性的(non-deterministic) 的task函数(给
定相同输入的情况下，它的输出不保证相同)。 此例中执行这个函数的副作用就是，每次task在
它的执行过程中都会随机地停某些秒
"""""
'''''
import gevent
import random

def task(pid):

    """""
    Some non-deterministic task
    """""
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchoronous():
    threads = [gevent.spawn(task,i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchorous:')
asynchoronous()
'''''
"""""
上例中，在同步的部分，所有的task都同步的执行， 结果当每个task在执行时主流程被阻塞(主流
程的执行暂时停住)。
程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。 初始化的greenlet列表存放
在数组threads中，此数组被传给gevent.joinall 函数，后者阻塞当前流程，并执行所有给定的
greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。
要重点留意的是，异步的部分本质上是随机的，而且异步部分的整体运行时间比同步 要大大减
少。事实上，同步部分的最大运行时间，即是每个task停0.002秒，结果整个 队列要停0.02秒。而
异步部分的最大运行时间大致为0.002秒，因为没有任何一个task会 阻塞其它task的执行。
"""""

"""""
一个更常见的应用场景，如异步地向服务器取数据，取数据操作的执行时间 依赖于发起取数据
请求时远端服务器的负载，各个请求的执行时间会有差别。
"""""
import gevent.monkey
gevent.monkey.patch_socket()

import gevent

"""""
python 3.X版本是不需要安装：urllib2包的，urllib和urllib2包集合成在一个包了
那现在问题是：
在python3.x版本中，如何使用：urllib2.urlopen()？
答：
import urllib.request
resp=urllib.request.urlopen("http://www.baidu.com")
"""""
import urllib.request
# pip install simplejson
import simplejson as json


def fetch(pid,postid):
    """""
    淘宝商品搜索建议:
    http://suggest.taobao.com/sug?code=utf-8&q=商品关键字&callback=cb 用例 
    ps:callback是回调函数设定
    """""
    #url = 'http://suggest.taobao.com/sug?code=utf-8&q=%s&callback=cb' % (name)
    url = 'http://www.kuaidi100.com/query?type=shunfeng&postid=%s' % (postid)
    #print(url)
    response = urllib.request.urlopen(url)
    result = response.read()
    json_result = json.loads(result)
    msg = json_result['message']
    print('Process %s %s ' % (pid,msg))
    return json_result['message']

def synchronous():
    #names = ['电脑', '手机', '眼镜', '男衣', '女衣', '皮包', '鞋子', '玩具', '电器', '书']
    #names = ['PC', 'Mobile', 'Glass', 'man', 'woman', 'bag', 'shoes', 'joy', 'car', 'book']
    post_id = ['1111111', '11111112', '1131111', '1411111', '5111111', '1111116', '1111171', '1181111', '1111190', ]
    for i in range(1,10):
        fetch(i,post_id[i-1])

def asynchronous():
    threads = []
    # names = ['电脑','手机','眼镜','男衣','女衣','皮包','鞋子','玩具','电器','书']
    #names = ['PC', 'Mobile', 'Glass', 'man', 'woman', 'bag', 'shoes', 'joy', 'car', 'book']
    post_id = ['1111111','11111112','1131111','1411111','5111111','1111116','1111171','1181111','1111190',]
    for i in range(1,10):
        threads.append(gevent.spawn(fetch,i,post_id[i-1]))
    gevent.joinall(threads)

print('Synchronous:')
#synchronous()

print('Asynchronous:')
asynchronous()

