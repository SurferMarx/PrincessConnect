import tkinter as tk
import os
import random
import pickle
import ret
import time
import os
import sys

#l1=[0]*144
#所有图片的回调函数
counter = 0
choose=[]
def callback(event):
    global counter
    global choose
    counter+=1
    #选中图片大于两个
    if(counter>2):
        for canva in canva_files:
            if canva!=0:
                canva.configure(bg=bgcolor)
        
        choose.clear()
        
        try:
            canva_files.index(event.widget)
        except ValueError:

            pass
        else:
            event.widget['bg'] = 'yellow'
            choose.append(event)
            counter=1
    else:
        try:
            canva_files.index(event.widget)
        except ValueError:
            # print('这里为空')
            pass
        else:
            event.widget['bg'] = 'yellow'
            choose.append(event)
    #选择第二个图片的时候判断能否与第一个消去
    if counter == 2:
        try:
            index1=canva_files.index(choose[0].widget)
            index2=canva_files.index(choose[1].widget)
        except (ValueError,IndexError):
            # print('ValueError')
            pass
        else:
            ret.getCan(canva_files)
            ifcan=ret.remove(index1,index2) and (image_names[index1]==image_names[index2]) 

            if ifcan:
                choose[0].widget.delete('photo')
                choose[1].widget.delete('photo')
                choose[0].widget['bg'] = bgcolor
                choose[1].widget['bg'] = bgcolor
                show_FireWork(choose,index1,index2)
                
                canva_files[index1]=0
                canva_files[index2]=0
                image_names[index1]=0
                image_names[index2]=0
    ##            print(canva_files)
    ##            print(image_names)
    
def show_FireWork(choose,index1,index2):
    global FireWork_files
    choose[0].widget.create_image(33.5*0.78,33.5*0.78,image=FireWork_files[16],tag='fireWork')
    choose[1].widget.create_image(33.5*0.78,33.5*0.78,image=FireWork_files[16],tag='fireWork')
    for i in range(len(FireWork_files)-1):
        time.sleep(0.01)
        choose[0].widget.delete('fireWork')
        choose[1].widget.delete('fireWork')
        choose[0].widget.create_image(26,26,image=FireWork_files[i+1],tag='fireWork')
        choose[1].widget.create_image(26,26,image=FireWork_files[i+1],tag='fireWork')
        window.update()
    choose[0].widget.delete('fireWork')
    choose[1].widget.delete('fireWork')

def NewGame():
    print("NewGame")
    global si
    si=0
    pickle_file = open('si.pickle', 'wb')
    pickle.dump(si, pickle_file)
    pickle_file.close()
    #打开新的游戏界面
    window.destroy()
    cwd=os.getcwd()
    os.system(cwd+"\demo6.py")

def SaveGame():
    print("SaveGame")
    pickle_file = open('todo.pickle', 'wb')
    pickle.dump(image_names, pickle_file)
    pickle_file.close()
    pickle_file2 = open('files.pickle', 'wb')
    pickle.dump(files, pickle_file2)
    pickle_file2.close()
    # 保存变量si
    global si
    si=1
    pickle_file = open('si.pickle', 'wb')
    pickle.dump(si, pickle_file)
    pickle_file.close()
    #保存并重新打开游戏界面
    window.destroy()
    cwd=os.getcwd()
    os.system(cwd+"\demo6.py")

def LoadGame():
    print("LoadGame")  

    pickle_file = open('todo.pickle', "rb")
    image_names_log = pickle.load(pickle_file)
    # print(image_names_log)
    pickle_file.close()
    for i in range(len(image_names_log)):
        if image_names_log[i] == 0:
            try:
                canva_files[i].delete('photo')
                canva_files[i].widget['bg'] = bgcolor
            except AttributeError:
                pass
            canva_files[i]=0
            image_names[i]=0

    i=0
    for item in image_names_log:
        if item==0:
            i+=1
        
    # print(i)
    # print(image_names_log)
    # window.update_idletasks()
    # window.update()


#打开变量si，判断是重新开始还是继续游戏
pickle_file_si = open('si.pickle', "rb")
si = pickle.load(pickle_file_si)
pickle_file_si.close()
if si==0:
    # 获得长度为100的files随机列表
    filename = os.listdir("change")
    random.shuffle(filename)
    ls1=filename[:10]*4
    ls2=filename[10:]*6
    files=ls1+ls2
    random.shuffle(files)
else:
    #加载上次的图片列表
    pickle_file = open('files.pickle', "rb")
    files = pickle.load(pickle_file)
    pickle_file.close()



window = tk.Tk()
window.title('PrinXConnect')
window.geometry('900x600')

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=NewGame)
filemenu.add_command(label='Save', command=SaveGame)
filemenu.add_command(label='Load', command=LoadGame)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)

bgcolor= window.cget("background")

#摆放Frame
frameKong = tk.Frame(window,height=500*0.05,width=600)
frameKong.pack()
frame = tk.Frame(window,height=800*0.75,width=800*0.75)

#图片列表
image_files=[tk.PhotoImage(file='./change/'+file) for file in files]
Ffiles = os.listdir("firework")
FireWork_files=[tk.PhotoImage(file='./firework/'+file) for file in Ffiles]
#tk.Canvas列表
canva_files=[]
#图片名列表与tk.Canvas列表一一对应，用来判断是否使同一种图片
image_names=[file for file in files]#image_names与canva_files相应位置元素一一对应

k=0
for i in range(10):
    for j in range(10):
        canva = tk.Canvas(frame,height=62*0.75, width=62*0.75)
        canva.bind("<Button-1>", callback)#绑定回调函数
        canva_files.append(canva)
        image = canva.create_image(33.5*0.78,33.5*0.78,image=image_files[k],tag='photo')
        canva.grid(row=i, column=j, padx=1, pady=1, ipadx=1, ipady=1)#摆放
        k+=1
        
        
#加一圈零
canva_files2=[0]*12
for i in range(10):
    canva_files2.append(0)
    canva_files2=canva_files2+canva_files[i*10:10+i*10]
    canva_files2.append(0)
canva_files2=canva_files2+[0]*12
canva_files=canva_files2
#print(canva_files)
#与tk.Canvas列表对应
image_names2=[0]*12
for i in range(10):
    image_names2.append(0)
    image_names2=image_names2+image_names[i*10:10+i*10]
    image_names2.append(0)
image_names2=image_names2+[0]*12
image_names=image_names2
#print(image_names)


frame.pack()
window.config(menu=menubar)
window.mainloop()
