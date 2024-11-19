# def 123(): # identifier rule is failed
#     print('hi')

def _123(): # identifier rule is not failed
    print('hi')

def _():
    print('hi')

def h():
    print('hello')
    print('i am a part of h function')

print('i am not a part of h function')