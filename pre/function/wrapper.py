#装饰器
#如果说我们想记录一个函数执行的时间，而我们又要多次执行这个函数
#那么我们可以用装饰器装饰函数，从而避免重复
#重复的代码是万恶之源

import time
import random

from functools import wraps

def record_time(func):

    @wraps(func)  #控制是否进行修饰
    def wrapper(*args,**kwargs):  #通过可变参数和关键字参数全部接纳
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间:{end-start:.2f}秒')
        return result
    return wrapper

#语法糖

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

download.__wrapped__('mysql')