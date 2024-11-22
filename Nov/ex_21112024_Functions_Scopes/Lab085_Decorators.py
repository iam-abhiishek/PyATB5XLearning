def add_extra_security_decorators(func):
    # def wrapper():

        print("1.Before the function is called.")
        print("2.Add Helmet, Dashcash, gloves, knee guards, License")
        func()  # # driving_scooty()
        print("3.After the function is called.")
        print("4.Secure Driving, Leave all the items")

    # return wrapper()

@add_extra_security_decorators
def ola_scooter():
    print('ola')



@add_extra_security_decorators
def driver_scooty():
    print('Normal function')
    print('I am driving a scooty')
