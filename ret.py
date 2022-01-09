#消去实现算法函数
canva_files=[]
Side_length=12
def getCan(canvas):
    global canva_files
    canva_files=canvas
#一维序号转二维序号
def change(index):
    index=index+1
    chushu=index//Side_length
    yushu=index%Side_length
    if yushu==0:
        y=chushu
        x=Side_length
    else:
        y=chushu+1
        x=yushu
#    print('(',x,',',y,')')
    return x,y
def change2(x,y):
    index=(y-1)*Side_length+x-1
    return index
#位置index是否有障碍物
def isBlocked(x,y):
    global canva_files
    index=(y-1)*Side_length+x-1
    if canva_files[index]==0:
        return 0             #无障碍物
    else: 
        return 1             #有障碍物
#垂直检测
def vertical(index1,index2):
    x1,y1=change(index1)
    x2,y2=change(index2)
    if x1 == x2 and y1 == y2:
        return False
    if x1 != x2:
        return False
    start_y=min(y1, y2)
    end_y  =max(y1, y2)
    for i in range(start_y+1,end_y):
        if isBlocked(x1, i):
            return False
    return True
#水平检测
def horizon(index1,index2):
    x1,y1=change(index1)
    x2,y2=change(index2)
    if x1 == x2 and y1 == y2:
        return False
    if y1 != y2:
        return False
    start_x=min(x1, x2)
    end_x  =max(x1, x2)
    for i in range(start_x+1,end_x):
        if isBlocked(i, y1):
            return False
    return True
#一个拐角
def turn_once(index1,index2):
    x1,y1=change(index1)
    x2,y2=change(index2)
#    print('(',x1,',',y1,')')
#    print('(',x2,',',y2,')')
    if x1 == x2 and y1 == y2:
        return False
    c_x = x1
    c_y = y2
    d_x = x2
    d_y = y1
    indexC=change2(x1,y2)
    indexD=change2(x2,y1)
    retC,retD=False,False
    if not isBlocked(c_x, c_y):
        retC = horizon(index2, indexC) and vertical(indexC, index1)
#        print('c',horizon(index2, indexC),vertical(indexC, index1))
#        print('c',retC)
    if not isBlocked(d_x, d_y):
        retD = horizon(index1, indexD) and vertical(indexD, index2)
#        print('d',horizon(index1, indexD),vertical(indexD, index2))
#        print('d',retD)
    if retC or retD:
        return True
    return False

#两个拐角
def turn_twice(index1,index2):
    x1,y1=change(index1)
    x2,y2=change(index2)
#    print('(',x1,',',y1,')')
#    print('(',x2,',',y2,')')
    if x1 == x2 and y1 == y2:
        return False
    for i in range(1,Side_length+1):
        for j in range(1,Side_length+1):
            if i != x1 and i != x2 and j != y1 and j != y2:
                continue
            if (i == x1 and j == y1)or(i == x2 and j == y2):
                continue
            if isBlocked(i, j):
                continue
            indexIJ=change2(i,j)
            if turn_once(index1, indexIJ) and ( horizon(indexIJ, index2) or vertical(indexIJ, index2) ):
                return True
            if turn_once(index2, indexIJ) and ( horizon(indexIJ, index1) or vertical(indexIJ, index1) ):
                return True
    return False

#remove最终函数
def remove(index1,index2):
    # x1,y1=change(index1)
    # x2,y2=change(index2)
    ret = False
    ret=horizon(index1,index2)
    if ret:
        return 1
    ret=vertical(index1,index2)
    if ret:
        return 1
    ret=turn_once(index1,index2)
    if ret:
        return 1
    ret=turn_twice(index1,index2)
    if ret:
        return 1
    
    return 0#不可到达