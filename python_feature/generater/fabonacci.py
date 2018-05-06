#Date:2018/5/6
#Author:dylan_xi
#Desc:use the example of fabonacci to describe why python need generater,
#     and how to use it 
# 

 
'''
(1) 
    how to create the series of fabonacci ? we can easily write the following code.
'''
def fab1(max):
    n , a , b = 1 , 1 , 1
    while n <= max:
        print(a)
        a , b = b , a + b
        n = n + 1
print("fab1:")
fab1(5)

'''
(2)
    As we can see , the code of (1) has low reuseability . To get the output series , we implant the print
    function into our fab function . We can't even get the series of fabonacci in other function. Because it returns 
    None.  
    In order to improve the reuseability of fab function , we can write the following code.
    It returns a list that contains the fabonacci series.
''' 
def fab2(max):
    result = []
    n , a , b = 1 , 1 , 1
    while n <= max:
        result.append(a)
        a , b = b , a + b
        n = n + 1    
    return result

print("fab2:")
print(fab2(5))

#we can also use for loop statement to print the list that fab2 function returns 
for x in fab2(5):
    print(x)

'''
(3)
    it seems that fab2 function works perfectly fine, but  experienced progammerers will indicate that 
    if the number is big , the function will cost big memory.If we want to controll the use of memery,
    it's best not to return list. 
    maybe we should retain the intermediate result?
    yes! we can use iterator to resovle the problem. for example:
        for i in range(10000): pass
    range() functon will return a 10000 list.
        for i in xrange(10000): pass
    xrange() function will return a iterable object.
    we can change fab function to a iterable class , we can see following the code    
''' 
class Fab3():
    def __init__(self , max):
        self.max = max
        self.n , self.a , self.b = 1 , 1, 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= self.max:
            r = self.a
            self.n = self.n + 1
            self.a ,  self.b = self.b , self.a +self.b
            return r
        raise StopIteration()
print('fab3:')
for n in Fab3(5):
    print(n)

'''
(4)
    Iterable class reslove the problem of cost memery . But it seems a little complex , isn't it?
    Luckily ,python provide the feature yield. yield change a function into a generator.
    python interpreter will regard it as a generator. when we call fab(5) , python will not execute function
    ,it'll return a iterable object. When excute for-loop statement , the function will be executed until yeild statement
    ,then it'll be interrupted. It returns current iterate value . In next iteration , function will start with the next statement of yeild ,
    The funciton' s local variable will be the same as the last time interruption. it will be interrupted when the next yeild statement excuted    
'''
def fab4(max):
    n , a , b = 1 , 1 , 1
    while n <= max:
        yield a
        a , b = b , a + b
        n = n + 1    

print('fab4:')
for n in fab4(5):
    print(n)

'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 
语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 
中断了数次，每次中断都会通过 yield 返回当前的迭代值。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next()
的值，不仅代码简洁，而且执行流程异常清晰。
quote from blog:"https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/index.html"
'''

'''
(5) 
    use generater to read data from file , if we read the file directly , it will
    cause unpredictable memery use. the best way is to use fixed-lenght buffer , loop read the whole
    file into the buffer. if we use yeild , oh my god ! it's so damn easy!!!
    we don't to write a iterator class to read file. 
'''


def read_file(fpath):
    BLOCK_SIZE =  1024
    with open(fpath , 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

for data in read_file('test.txt'):
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print(data)