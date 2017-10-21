def f1(a):                       
    print('in f1 a=',a)
    def f2(func):
        print('in f2 func=',func)
        def f3(*args, **kwargs):
            func()
            print(' in f3 a=  ', a)
            print(' in f3 func=  ', func)
            print(' in f3', *args, **kwargs)
        return f3
    return f2

def t1(func):
    def t2(*args):
        print(func,  args)
    return t2

@t1('laowang')
#@f1('laowang')
def tmp():
    print(' 被装饰的函数执行了...  ')


tmp()
