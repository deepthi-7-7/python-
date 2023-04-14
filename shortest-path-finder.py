import curses
from curses import wrapper
import queue 
import time

maze=[["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]]


def get_maze(maze,stdsrc,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)
    
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j)in path:
                stdsrc.addstr(i,j*2,"X",RED)
            else:
                stdsrc.addstr(i,j*2,value,BLUE)


def find_start(maze,start):
    for i,row in enumerate(maze):
        for j, value in enumerate(row):
            if value==start:
                return i,j
    return None

def find_path(maze,stdsrc):
    start="O"
    end="X"
    start_pos=find_start(maze,start)

    q=queue.Queue()
    q.put((start_pos,[start_pos]))   #here we have two parameters one shows the start position and other shows the path

    visited=set()

    while not q.empty():
        current_pos,path=q.get()  #it will get you the most recent position and the current path
        row,col=current_pos    #we are making the current position into two parts i.e, row and column in order to search the different nodes to find a path
        

        stdsrc.clear()
        get_maze(maze,stdsrc,path)
        # stdsrc.addstr(6,11,"hello")

        time.sleep(0.3)
        stdsrc.refresh()
        

        if maze[row][col]==end:
            return path
        
        neighbors=find_neighbors(maze,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r,c = neighbor
            if maze[r][c]=="#":
                continue

            new_path=path+[neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)


def find_neighbors(maze,row,column):
    neighbors=[]
    if row>0: #UP
        neighbors.append((row-1,column))
    if row+1<len(maze): #DOWN
        neighbors.append((row+1,column))
    if column>0: #LEFT
        neighbors.append((row,column-1))
    if column+1<len(maze[0]): #RIGHT
        neighbors.append((row,column+1))

    return neighbors


#stdsrc means standard screen
def main(stdsrc):
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    find_path(maze,stdsrc)
    stdsrc.getch()

wrapper(main)
