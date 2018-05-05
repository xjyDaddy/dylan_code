#Date:2018/5/5
#Author:dylan_xi
#Desc:use dfs to  implment permutation

class Permutation():
    def __init__(self , array):
        self._array = array
        self._book = [0] * len(array)
        self._logPath =  [-1] * len(array)
        self._result = []
    def _dfs(self , n):
        if n >= len(self._array):
            #add one result , attention:(must make a new list to 
            # storage result ,otherwise all the result reference the newest logpath) 
            oneResult = []
            oneResult.extend(self._logPath)
            self._result.append(oneResult)
            return 
        for index in range(0 , len(self._array)):
            #if the index is't be used , use it
            if self._book[index] == 0:
                self._logPath[n] = self._array[index]
                #book the use of index 
                self._book[index] = 1
                #to the next step dfs
                self._dfs(n+1)
                #give back the use of index , so that next step dfs can reuse it!
                self._book[index] = 0
    def getResult(self):
        self._book = [0] * len(array)
        self._result.clear()
        self._dfs(0)
        return self._result

if __name__ == '__main__':
    array =['A','B','C','D','E']
    result = Permutation(array).getResult()
    print(result)