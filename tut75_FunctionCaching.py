import functools
import time 
from functools import lru_cache

"""function caching is a process of storing return value of a function, taking some time to complete, and using the variable instead of function call over and over again."""

# @lru_cache(maxsize=3)
# def some_work(n):
#     """this function do some task taking n seconds."""
#     time.sleep(n)
#     return n

# quiz
inp = int(input('Enter max chace size: '))
@lru_cache(maxsize=inp)
def time_delay(n):
    """this function do some task taking n seconds."""
    print('running')
    time.sleep(n)
    return n

if __name__ == '__main__':
    # print('now running some work')
    # some_work(3)# take time
    # print('done first time, calling again....')
    # some_work(1)# take time
    # print('done second time, calling again....')
    # some_work(3)# happen quickly
    # print('done third time, calling again....')
    # some_work(2)# take time
    # print('done fourth time, calling again....')
    # some_work(1)# happen quickly
    # print('done fifth time, calling again....')
    time_delay(3)
    print('ran')
    time_delay(3)
    if inp>=1:
        print('memory is cached...')
    else:
        print('no memory in cached')
