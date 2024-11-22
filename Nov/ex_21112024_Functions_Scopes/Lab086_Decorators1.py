def add_decor1(func):
    def wrapper():
        print('before running the UI IC')
        print('start the browser')
        func()
        print('after running the UI IC')
        print('close the browser')
    return wrapper()



@add_decor1
def test_ui():
    print('hi')