#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:58:37 2019

@author: TianyangWen
"""

import tkinter as tk
import sys
import os
import time

workpath = os.path.split(os.path.realpath(sys.argv[0]))[0]

with open(workpath+'/names.txt','r') as f:
    names=f.readlines()
for i in range(len(names)-1,-1,-1):
    if len(names[i])==0:
        del names[i]
        continue
    elif names[i][-1]=='\n':
        names[i]=names[i][:-1]    
#names1=names.copy()
#for i in range(20):
#    names1.append('谭松柏')  
counter = 0    

def counter_label(label):
    def count():
        global counter
        global s
        counter += 1
        #label.config(text=names1[counter%len(names1)])
        label.config(text=names[counter%len(names)])
        s=label.after(50, count)
    count()

def appear(index, letter):
    if buttons[index]['fg']=='white':
        buttons[index]['fg']='green'
        buttons[index]['bg']='white'
    else:
        buttons[index]['fg']='white'
        buttons[index]['bg']='orange'

def save(event):
    local_time=time.strftime('%Y.%m.%d',time.localtime(time.time()))
    absent_list=[local_time+'\n']
    for i in range(len(names)):
        if buttons[i]['bg']=='orange':
            absent_list.append(names[i])
    with open(workpath+'/result_'+local_time+'.txt','w',encoding='utf-8') as f:
        f.writelines(absent_list)
    event.widget['text']='Saved'
    event.widget['state'] = 'disabled'

def Pause():
    global label
    if button1['text']=='Stop':
        label.after_cancel(s)  
        button1['text']='Restart'
        #print('开始')
    else:
        label = tk.Label(win, fg="green",bg='yellow',font=("kaiti", 30),height=2,width=10)
        label.grid(row=1,column=9,columnspan=2,rowspan=2)
        counter_label(label)
        button1['text']='Stop'

  

win=tk.Tk()
win.title('Educational Assistance System')
win.geometry('850x480')
#win.resizable(False, False) 


   
#############作业统计
buttons = []

for index in range(len(names)): 
    n=names[index]
    button = tk.Button(win, fg="white",bg='orange',relief='raised', padx=0.1,font=("heiti", 15,'bold'),text=n,height=2,width=8, command=lambda index=index, n=n: appear(index, n))
    # Add the button to the window
    button.grid(padx=2, pady=2, row=index//6, column=index%6)
    # Add a reference to the button to 'buttons'
    buttons.append(button)
    
############随机点名
label = tk.Label(win, fg="green",bg='yellow',font=("kaiti", 30),height=2,width=10)
label.grid(row=1,column=9,columnspan=2,rowspan=2)
counter_label(label)
button1 = tk.Button(win, text='Stop',bg='pink',fg='green',relief='raised',width=10, command=Pause)
button1.grid(row=3,column=9,columnspan=2)
#############存储作业名单
save_button=tk.Button(win,text='Save',bg='pink',fg='green',height=2,width=10)
save_button.grid(row=5,column=9,columnspan=2)
save_button.bind('<Button-1>', save)
label_author = tk.Label(win, text='@author: TianyangWen',fg="black",font=("Songti", 10),height=2,width=20,anchor='s')
label_author.grid(row=7,column=10,columnspan=2,rowspan=2)
win.mainloop()
