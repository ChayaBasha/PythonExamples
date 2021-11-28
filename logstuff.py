from functools import wraps
# Online Python - IDE, Editor, Compiler, Interpreter


def logStuff(func):
    @wraps(func)
    def loggerAndExec(*args, **kwargs):
        print("Args to", func.__name__, end=' ')
        print(*args, sep=" & ")
        ret = func(*args, **kwargs)
        print(func.__name__, "Returning", ret)
        return ret
    return loggerAndExec

@logStuff
def sum(a, b):
    return (a + b)

@logStuff
def sub(a, b):
    return a - b
    
print(sum)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

sum(a, b)
sub(a, b)
