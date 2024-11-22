import time
def time_decor(func):

    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        # print('total time taken by func', end_time - start_time)
    return wrapper()


def print_logs(func):
    def wrapper():
        print('starting logs')
        func()
        print('ending logs')
    return wrapper()



@time_decor
@print_logs
def time_1():
    print('time taken by function 1')
    time.sleep(2)


@time_decor
def time_2():
    print('time taken by function 2')
    time.sleep(5)


