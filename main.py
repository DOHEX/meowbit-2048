from meowbit import *
import random

screen.sync=0
screen.fill((250, 248, 239))
screen.rect(0,0,128,128,(187, 173, 160))
screen.refresh()

block_color = {  
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
            4096: (60, 58, 50),
            8192: (60, 58, 50)
        }
nums_color = {
            0: (205, 193, 180),
            2: (0, 0, 0),
            4: (0, 0, 0),
            8: (255, 255, 255),
            16: (255, 255, 255),
            32: (255, 255, 255),
            64: (255, 255, 255),
            128: (255, 255, 255),
            256: (255, 255, 255),
            512: (255, 255, 255),
            1024: (255, 255, 255),
            2048: (255, 255, 255),
            4096: (255, 255, 255),
            8192: (255, 255, 255)
        }
        
blocks=[[0 for i in range(4)] for j in range(4)]
last_blocks=[]
changed=False


def up():
    global changed
    last_blocks=copy.deepcopy_blocks
    for x in range(4):
        k=0
        for y in range(1,4):
            if blocks[x][y]>0:
                if blocks[x][k]==blocks[x][y]:
                    blocks[x][k]+=blocks[x][y]
                    blocks[x][y]=0
                    changed=True
                    k=k+1
                elif blocks[x][k]==0:
                    blocks[x][k]=blocks[x][y]
                    blocks[x][y]=0
                    changed=True
                else:
                    blocks[x][k+1]=blocks[x][y]
                    if(y!=k+1): 
                        blocks[x][y]=0
                        changed=True
                    k=k+1
    Randomer()
    drawBlk()
def down():
    global changed
    last_blocks=copy.deepcopy_blocks
    for x in range(4):
        k=3
        for y in range(2,-1,-1):
            if blocks[x][y]>0:
                if blocks[x][k]==blocks[x][y]:
                    blocks[x][k]+=blocks[x][y]
                    blocks[x][y]=0
                    k=k-1
                    changed=True
                elif blocks[x][k]==0:
                    blocks[x][k]=blocks[x][y]
                    blocks[x][y]=0
                    changed=True
                else:
                    blocks[x][k-1]=blocks[x][y]
                    if(y!=k-1): 
                        blocks[x][y]=0
                        changed=True
                    k=k-1
    Randomer()
    drawBlk()
def left():
    global changed
    last_blocks=copy.deepcopy_blocks
    for y in range(4):
        k=0
        for x in range(1,4):
            if blocks[x][y]>0:
                if blocks[k][y]==blocks[x][y]:
                    blocks[k][y]+=blocks[x][y]
                    blocks[x][y]=0
                    k=k+1
                    changed=True
                elif blocks[k][y]==0:
                    blocks[k][y]=blocks[x][y]
                    blocks[x][y]=0
                    changed=True
                else:
                    blocks[k+1][y]=blocks[x][y]
                    if(x!=k+1): 
                        blocks[x][y]=0
                        changed=True
                    k=k+1
                    
    Randomer()
    drawBlk()
def right():
    global changed
    last_blocks=copy.deepcopy_blocks
    for y in range(4):
        k=3
        for x in range(2,-1,-1):
            if blocks[x][y]>0:
                if blocks[k][y]==blocks[x][y]:
                    blocks[k][y]+=blocks[x][y]
                    blocks[x][y]=0
                    k=k-1
                    changed=True
                elif blocks[k][y]==0:
                    blocks[k][y]=blocks[x][y]
                    blocks[x][y]=0
                    changed=True
                else:
                    blocks[k-1][y]=blocks[x][y]
                    if(x!=k-1): 
                        blocks[x][y]=0
                        changed=True
                    k=k-1
                    
    Randomer()
    drawBlk()

sensor.btnTrig["up"] = up
sensor.btnTrig["down"] = down
sensor.btnTrig['left'] = left
sensor.btnTrig["right"] = right
    
def drawBlk():
    for x in range(4):
        for y in range(4):
            screen.rect(x*32+1,y*32+1,30,30,block_color[blocks[x][y]],1)
            if (blocks[x][y]<10):
                screen.text(blocks[x][y],x*32+8,y*32+9,2,nums_color[blocks[x][y]])
            elif(blocks[x][y]<100):  
                screen.text(blocks[x][y],x*32+8,y*32+12,1,nums_color[blocks[x][y]])
            elif(blocks[x][y]<1000): 
                screen.text(blocks[x][y],x*32+4,y*32+12,1,nums_color[blocks[x][y]])
            elif(blocks[x][y]<10000): 
                screen.text(blocks[x][y],x*32+0,y*32+12,1,nums_color[blocks[x][y]])
    screen.refresh()
    sleep(0.2)
    
def GetEmpty():
        list = []
        for x in range(4):
            for y in range(4):
                if blocks[x][y] == 0:
                    list.append([x, y])
        return list
        
def Randomer():
    global changed
    list =GetEmpty()  
    if list and changed:
        changed=False
        value = 2 if random.random() <0.9 else 4
        
        x, y = list[random.randint(0,len(list)-1)]
        blocks[x][y] = value
blocks[0][0]=2
blocks[0][1]=2
blocks[0][2]=4
blocks[0][3]=8
blocks[0][0]=2
blocks[1][1]=2
blocks[2][2]=4
blocks[3][3]=8
drawBlk()
