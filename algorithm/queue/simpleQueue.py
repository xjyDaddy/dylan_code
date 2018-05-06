#Date:2018/5/5
#Author:dylan_xi
#Desc:a simple queue demo

class SimpleQueue():
    def __init__(self , queueSize = 10):
        self._datas = [1]*queueSize
        self._head = 0
        self._tail = 0
        self._size = 0
        self._queueSize = queueSize
    def getSize(self):
        return self._size

    #push data in the tail , if queue is full
    # it'll cover data in the head  
    def push(self , data):
        if self._tail >= self._queueSize:
            self._tail = 0
        if self._tail == self._head:
            self._head = self._head + 1
            if self._head >= self._queueSize:
                self._head = 0
        self._datas[self._tail] = data
        self._tail = self._tail + 1
        self._size = self._size + 1
        if self._size >= self._queueSize:
            self._size = self._queueSize

    #pop data in the head , if queue is empty , nothing will happen             
    def pop(self):
        if self._size == 0:
            return
        self._head = self._head + 1
        if self._head >= self._queueSize:
            self._head = 0
        self._size = self._size - 1
    def getFront(self):
        return self._datas[self._head]
    
    def getBack(self):
        if self._tail >= self._queueSize:
            return self._datas[0]
        return self._datas[self._tail -1]
    def isFull(self):
        return self._size >= self._queueSize
    def isEmpty(self):
        return self._size == 0


#test queue
print("test begin ...")
testQueue = SimpleQueue(5)
assert(testQueue.isEmpty())
testQueue.push(1)
testQueue.push(2)
assert(testQueue.getSize() == 2)
assert(testQueue.getFront() == 1)
assert(testQueue.getBack() == 2)
testQueue.push(3)
testQueue.push(4)
testQueue.push(5)
assert(testQueue.isFull())
testQueue.push(6)
assert(testQueue.getFront() == 2)
assert(testQueue.isFull())
testQueue.pop()
assert(testQueue.getFront() == 3)
assert(testQueue.getBack() == 6)
testQueue.pop()
testQueue.pop()
testQueue.pop()
testQueue.pop()
assert(testQueue.getSize() == 0)
print("test success ...")