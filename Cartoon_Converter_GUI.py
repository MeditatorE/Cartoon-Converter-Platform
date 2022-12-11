# this file use to create GUI for Cartoon style convert

import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter.ttk import *
import subprocess
from shutil import copy
from tkinter import filedialog
from tkinter import messagebox
from chevereto import upload_to_chevereto

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

window.button_upload = Button(window, text="Batch Upload", width=10)
window.button_upload.place(x=110, y=540)

window.button_start = Button(window, text="Start Convert", width=10)
window.button_start.place(x=350, y=540)

window.button_clear = Button(window, text="Display Picture", width=10)
window.button_clear.place(x=580, y=540)

# 5. set combox

value = StringVar()
value.set('Hosoda')
values = ['Hosoda', 'Shinkai', 'Paprika', 'Hayao']
combobox = Combobox(
    master=window,  # 父容器
    height=10,  # 高度,下拉显示的条目数量
    width=10,  # 宽度
    state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
    font=('', 15),  # 字体
    textvariable=value,  # 通过StringVar设置可改变的值
    values=values,  # 设置下拉框的选项
)
combobox.place(x=350, y=400)


# 6. set hyperlink and text

def callback1(event):
    # need to modify the link
    webbrowser.open_new("http://jellyfin.orangetien.icu:1500/")


link1 = tk.Label(window, text="Go to Platform", fg="grey")
link1.place(x=598, y=585)
link1.bind("<Button-1>", callback1)


def callback2(event):
    ans = messagebox.askyesno("Message","Are you sure you want to upload all your pictures?")
    # return True/False
    path = "./store"
    if (ans == True):
        # upload pictures to platform
        upload_to_chevereto(path)
        i = 0
        # clear the folder
        path_dir = os.listdir(path)
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if (i > 0):
                os.remove(full_path)
        messagebox.askokcancel("Message","Done! The picture has been uploaded, thanks for your contribution！")
    if (ans == False):
        i = 0
        # clear the folder
        path_dir = os.listdir(path)
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if (i > 0):
                os.remove(full_path)



link2 = tk.Label(window, text="Update pictures to platform!",underline=1, fg="Blue")
link2.place(x=325, y=585)
link2.bind("<Button-1>", callback2)


def callback3(event):
    # need to modify the link
    webbrowser.open_new("http://jellyfin.orangetien.icu:1499/")


link3 = tk.Label(window, text="Manual", fg="grey")
link3.place(x=148, y=585)
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
    
    # clear folder "store"
    delete_path="./store"
    path_dir = os.listdir(delete_path)
    j = 0
    for filename in path_dir:  # 遍历pathDir下的所有文件filename
        j = j + 1
        full_path = os.path.join(delete_path, filename)  # 文件的绝对路径(包含文件的后缀名)
        if (j > 0):
            os.remove(full_path)

    
    # select the style
    style = combobox.get()

    cmd = 'python test.py --input_dir ./Upload --style ' + style + ' --gpu -1'
    os.system(cmd)

    file_path = "./store"
    save_path = "./Result"

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
    if (t > 1):
        path1 = "./Result"
        subprocess.call(["open", path1])
    if (t == 1):
        fileName = os.path.splitext(filename)[0]
        filepath = "./Result/" + fileName + "_" + style + ".jpg"
        subprocess.call(["open", filepath])
    
    # 弹出会话框
    ans = messagebox.askyesno("Message","Do you want to delete the picture you just uploaded?")
    # 返回值为True或者False
    if (ans == True):
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







