#Date:2018/5/5
#Author:dylan_xi
#Desc:use dfs to judge equation
'''
    用 1 2 3 4 5 6 7 8 9 九个数组成等式:
    [][][] + [][][] = [][][]
    不能重复使用数字,打印出所有的可能性
'''
#book the use of numbers 
book = [0] * 11 
log =  [0] * 10
def dfs(n):
    if n >= 9:
        if log[0]*100 + log[1]*10 + log[2] + log[3]*100 + log[4]*10 + log[5] == log[6]*100 + log[7]*10 + log[8]: 
            print("{0[0]}{0[1]}{0[2]} + {0[3]}{0[4]}{0[5]} = {0[6]}{0[7]}{0[8]}".format(log))
        return
    for number in range(1 ,10):
        if book[number] == 0:
            book[number] = 1
            log[n] = number
            dfs(n+1)
            book[number] = 0

dfs(0)
