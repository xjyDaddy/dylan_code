#Date:2018/5/6
#Author:dylan_xi
#Desc:use dfs to find target in maze
'''
    in a bivariate maze , for exmaple:
                [3 0 0 0 0]
                [1 0 0 1 0]
                [0 0 1 0 0]
                [1 1 0 1 2]
                [0 0 0 0 0]
    0 stands for passable road, 1 stands for obstacle that we can not pass, 3 stands for where we are , 2
    stands for target position we want to go.we can only move one grid in one step,
    hero is the question:
        find the minimum step need , that move from where we are to the target position 
'''

#represent right,down,left,up
next = [[1,0] , [0,-1] , [-1,0] , [0,1]]
#represent maze
maze = [[3,0,0,0,0],[1,0,0,1,0],[0,0,1,0,0],[1,1,0,1,2],[0,0,0,0,0]]
mazeWidth = len(maze[1])
mazeHeight = len(maze)
#book the position that have moved
book =  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
minStep = 999999

def dfs(x , y , step):
    if maze[y][x] == 2:
        global minStep
        print("step:" + str(step))
        if step < minStep:
            minStep = step
        return
    for diff in next:
        nextX = diff[0] + x
        nextY = diff[1] + y
        if nextX >= 0 and nextX < mazeWidth and nextY >= 0 and nextY < mazeHeight:
            if book[nextX][nextY] == 0 and maze[nextY][nextX] != 3 and maze[nextY][nextX] != 1:
                book[nextX][nextY] = 1
                dfs(nextX , nextY ,step+1)
                #have to give back for the next try
                book[nextX][nextY] = 0
book[0][0] = 1
dfs(0 ,0 , 0)
print(minStep)