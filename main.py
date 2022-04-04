# this file use to create GUI for Cartoon style convert

import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter.ttk import *
import subprocess
from shutil import copy
from tkinter import filedialog


global t

# Set GUI

# 0. initialize

path = "./Upload/.DS_Store"
if os.path.exists(path):
    os.remove(path)

path = "./store/.DS_Store"
if os.path.exists(path):
    os.remove(path)


# 1. set window object

window = Tk()
window.geometry("808x630+200+100")
window.title('Cartoon Converter')
window.resizable(0, 0)
window["bg"] = "White"  # 白色



# 2. set sessions

# 此处采用 panedWindow 和 LabelFrame 容器控件
window.all_pane = PanedWindow(width=808, height=650)  # 这里是规定容器的长宽
window.all_pane.place(x=0, y=0)  # 这里是决定将这个容器放在哪个位置
# 这个坐标应该指的是左上角的点的位置



# 3. show the pictures

top_image = PhotoImage(file="comet.png")
top_label = Label(window, image=top_image)
top_label.place(x=0, y=0)

middle_image = PhotoImage(file="click1.png")
middle_label = Label(window, image=middle_image)
middle_label.place(x=160, y=125)
    


# 4. set button

window.button_upload = Button(window, text="Upload", width=10)
window.button_upload.place(x=150, y=530)

window.button_start = Button(window, text="Start", width=10)
window.button_start.place(x=350, y=530)

window.button_clear = Button(window, text="Display", width=10)
window.button_clear.place(x=550, y=530)



# 5. set combox

value = StringVar()
value.set('Hosoda')
values = ['Hosoda', 'Shinkai', 'Paprika', 'Hayao']
combobox = Combobox(
    master=window, # 父容器
    height=10, # 高度,下拉显示的条目数量
    width=10, # 宽度
    state='readonly', # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
    font=('', 15), # 字体
    textvariable=value, # 通过StringVar设置可改变的值
    values=values, # 设置下拉框的选项
)
combobox.place(x=350, y=400)



# 6. set hyperlink and text

def callback1(event):
    webbrowser.open_new("https://www.artstation.com/?sort_by=community")

link1 = tk.Label(window, text="Go to Platform", fg="grey")
link1.place(x=568, y=580)
link1.bind("<Button-1>", callback1)


def callback2(event):
    root = Tk()
    root.geometry("500x100")
    root.title('About us')
    text = Text(root, width=550, height=100)
    text.insert(INSERT, "                 Copyright@\n"
                        "                  Email: 15620242877@163.com\n"
                        "           Sun Chen, Zhou Yunpeng, Tian Jincheng, Chen Xinyun\n")
    text.place(x=0, y=0)
    text.configure(state="disabled")

link2 = tk.Label(window, text="About us", fg="grey")
link2.place(x=384, y=580)
link2.bind("<Button-1>", callback2)


def callback3(event):
    root = Tk()
    root.geometry("550x150")
    root.title('Manual')
    text = Text(root, width=550, height=150)
    text.insert(INSERT, "The first button 'upload' on the left is used to upload photos,\n"
                        "Then click the middle 'start' button, you will see the original photo,\n"
                        "the photo when you were young and the photo when you were old respectively.\n"
                        "The right button can clear the window for next uploading.\n")
    text.place(x=0, y=0)
    text.configure(state="disabled")

link3 = tk.Label(window, text="Manual", fg="grey")
link3.place(x=188, y=580)
link3.bind("<Button-1>", callback3)



# 7. Set mouse event detection

def callback4(event):
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    save_path = "./Upload"
    copy(file_path, save_path)

middle_label.bind("<Button-1>", callback4)


# 8. implement the button function

# implement button start

def start(*args):
    
    style=combobox.get()

    cmd = 'python test.py --input_dir ./Upload --style '+ style + ' --gpu -1'
    os.system(cmd)

    file_path = "./Result"
    save_path = "./store"

    path_dir = os.listdir(file_path)
    for filename in path_dir:  # 遍历pathDir下的所有文件filename
        from_path = os.path.join(file_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
        to_path = save_path  # 新文件的绝对路径
        copy(from_path, to_path)  # 完成复制黏贴

    path = "./Upload"
    path_dir = os.listdir(path)

    t = 0
    for filename in path_dir:  # 遍历pathDir下的所有文件filename
        t = t + 1
    if(t > 1):
        path1 = "./Result"
        subprocess.call(["open", path1])
    if(t == 1):
        fileName = os.path.splitext(filename)[0]
        filepath = "./Result/" + fileName + "_"+ style +".jpg"
        subprocess.call(["open", filepath])

    i = 0
    for filename in path_dir:  # 遍历pathDir下的所有文件filename
        i = i + 1
        full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
        if (i > 0):
           os.remove(full_path)
        
window.button_start.bind('<Button-1>', start)


# implement button clear
def display(*args):
    path = "./Result"
    subprocess.call(["open", path])

window.button_clear.bind('<Button-1>', display)


# implement button upload
def upload(*args):
    path = "./Upload"
    subprocess.call(["open", path])

window.button_upload.bind('<Button-1>', upload)

    
    
# 9. start GUI
window.mainloop()







