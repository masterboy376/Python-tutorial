# coroutines are used to avoid running a function again and again form the start, insted running it from the midway.


def searcher():
    """some task consuming 4 seconds"""
    import time
    book = ' this is sam book and good bad all together is neutral and we all should be neutral bcoz this is kal yuga and only good cannot survive mixture will go long way so be a mixture lad.'
    time.sleep(4)

    while True:# this will make this function a coroutine
        text = (yield)
        if text in book :
            print(f'{text} is in the book')
        else:
            print(f'{text} is not in the book')

search = searcher()# simply creating a instance of our coroutine
print('starting the searcher')
next(search)# starting the coroutine
print('search started')
input('press any key ')
search.send('good')# sending value to the coroutine
search.send('samb')# sending value to the coroutine
search.send('yuga')# sending value to the coroutine
print('closing the searcher')
search.close()#closes the coroutine
print('searcher closed')

