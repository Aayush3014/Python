#python closure

def make_copy(msg):
    msg = "Hello Everyone"

    def print_copy():
        msg = "welcome everyone"
        print(msg)

    print(msg)
    
    return print_copy

execute = make_copy("cccc")
execute()
execute()