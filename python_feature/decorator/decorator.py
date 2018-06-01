#!/usr/bin/env python
#Date:2018/5/28
#Author:dylan_xi
#Desc:learn python decorator
'''
def foo():
    print('call foo!')
'''
#we want to add new features into foo function, but we don't want to 
#mofidy foo function. we can create a new function and pass func as it's
#param
'''
def log(func):
    print('add log')
    func()

log(foo)
'''
#the problem is we have to change all the use of foo,maybe in everywhere,
#we hope to add new features and we don't want to cause any other changes
#we can use decorator as follows
'''
def log(func):
    def warp():
        print('add log')
        func()
    return warp

foo = log(foo)
foo()
'''
#in python we can simple do it like this:
#syntactic suger
'''
def log(func):
    def warp():
        print('add log')
        func()
    return warp
@log
def foo():
    print('call foo')
# we don't have add code: foo = log(foo)
foo()
'''
#*args、**kwargs
#if function foo need param
'''
def log(func):
    def warp(*args , **kwargs):
        print('add log')
        func(*args,**kwargs)
    return warp
@log
def foo(text):
    print('call foo:' , text)
# we don't have add code: foo = log(foo)
foo('dylan_xi')
'''

# if we want to add param to decorator
'''
def log(text):
    def decorator(func):
        def warp(*args , **kwargs):
            print('add log' , text)
            func(*args,**kwargs)
        return warp
    return decorator
@log(text = 'decotator param')
def foo(str):
    print('call foo:' , str)
# we don't have add code: foo = log(foo)
foo('dylan_xi')
'''
#we can alse use class as decorator, compared with function 
#decorator , class decorator is cohesiveness and encapsulation and flexible
'''
class log(object):
    def __init__(self,func):
        self._func = func

    def __call__(self):
        print('add log')
        self._func()

@log
def foo():
    print('foo called')

foo()
'''
#functools.wraps:(i use python36 , it seems i don't need this , python seems have done it internal)
#decorator make greate use of code , but the meta info of the function is lost
#such as:docstring、__name__.
#we can use functool.wraps to copy meta info into decorator function

def log(func):
    def warp():
        print('add log')
        print('func.__name__:',func.__name__)
        func()
        print('func.__name__:',func.__name__)
    return warp

@log
def foo():
    print('call foo')
foo()
