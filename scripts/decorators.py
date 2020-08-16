from datetime import datetime

def main_func():
    print("It as a main function")

def decor_func(function):
    def wrapper():
        if 6 <= datetime.now().hour < 13:
            print("It is a decor morning function")
        elif 13 <= datetime.now().hour < 24:
            print("It is a decor afternoon function")
        else:
            print("it is a decor night function")
        return(function)
    return wrapper()

decor_func(main_func())