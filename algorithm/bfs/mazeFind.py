#Date:2018/5/6
#Author:dylan_xi
#Desc:use bfs to find target in maze
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
#represent right,down,left,up3
next = [[1,0] , [0,-1] , [-1,0] , [0,1]]
#represent maze
maze = [[3,0,0,0,0],[1,0,0,1,0],[0,0,1,0,0],[1,1,0,1,2],[0,0,0,0,0]]
mazeWidth = len(maze[1])
mazeHeight = len(maze)
#book the position that have moved
book =  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
minStep = 999999
queue =[] 
def bfs(x,y):
    head = 0
    tail = 0
    queue.append({'x':x ,'y':y ,'parent': None , 'step':0})
    tail = tail +1
    book[x][y] = 1
    while(tail > head):
        currentX = queue[head]['x']
        currentY = queue[head]['y']
        head = head + 1
        for diff in next:
            nextX = diff[0] + currentX
            nextY = diff[1] + currentY
            if nextX < 0 or nextX >= mazeWidth or nextY < 0 or nextY >= mazeHeight:
                continue
            if book[nextX][nextY] == 0 and maze[nextY][nextX] != 3 and maze[nextY][nextX] != 1:
                book[nextX][nextY] == 1
                queue.append({'x':nextX ,'y':nextY ,'parent': queue[head-1], 'step': queue[head-1]['step'] +1})
                tail = tail + 1
            if maze[nextY][nextX] == 2:
                print(queue[head-1]['step']+1)
                return
bfs(0,0)