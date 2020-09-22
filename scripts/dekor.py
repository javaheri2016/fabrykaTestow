def decor(function):
    def inside():
        print('decorate function')
        return function()
    return inside()

@decor
def main_function():
    print('main function')
