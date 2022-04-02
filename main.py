# this file use to create GUI for Cartoon style convert

import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter.ttk import *
import subprocess
from PIL import Image
from PIL import ImageTk
from shutil import copy

global acc
acc = 0

while (acc < 1):

    # Set GUI

    # 0. initialize
    path = "./test_img/.DS_Store"
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
    window.all_pane = PanedWindow(width=808, height=630)  # 这里是规定容器的长宽
    window.all_pane.place(x=0, y=0)  # 这里是决定将这个容器放在哪个位置
    # 这个坐标应该指的是左上角的点的位置

    # 6. show the pictures

    top_image = PhotoImage(file="comet.png")
    top_label = Label(window, image=top_image)
    top_label.place(x=0, y=0)

    
    # 3. set button

    window.button_upload = Button(window, text="Upload", width=10)
    window.button_upload.place(x=150, y=530)

    window.button_start = Button(window, text="Start", width=10)
    window.button_start.place(x=350, y=530)

    window.button_clear = Button(window, text="Display", width=10)
    window.button_clear.place(x=550, y=530)


    
    # 4. set hyperlink

    def callback1(event):
        webbrowser.open_new("https://www.artstation.com/?sort_by=community")


    link1 = tk.Label(window, text="Go to Platform", fg="grey")
    link1.pack()
    link1.place(x=568, y=580)
    link1.bind("<Button-1>", callback1)


    def callback2(event):
        root = Tk()
        root.geometry("500x100")
        root.title('About us')
        text = Text(root, width=550, height=100)
        text.pack()
        text.insert(INSERT, "                 Copyright@\n"
                            "                  Email: 15620242877@163.com\n"
                            "           Sun Chen, Zhou Yunpeng, Tian Jincheng, Chen Xinyun\n")
        text.place(x=0, y=0)
        text.configure(state="disabled")


    link2 = tk.Label(window, text="About us", fg="grey")
    link2.pack()
    link2.place(x=384, y=580)
    link2.bind("<Button-1>", callback2)


    def callback3(event):
        root = Tk()
        root.geometry("550x150")
        root.title('Manual')
        text = Text(root, width=550, height=150)
        text.pack()
        text.insert(INSERT, "The first button 'upload' on the left is used to upload photos,\n"
                            "Then click the middle 'start' button, you will see the original photo,\n"
                            "the photo when you were young and the photo when you were old respectively.\n"
                            "The right button can clear the window for next uploading.\n")
        text.place(x=0, y=0)
        text.configure(state="disabled")


    link3 = tk.Label(window, text="Manual", fg="grey")
    link3.pack()
    link3.place(x=188, y=580)
    link3.bind("<Button-1>", callback3)




    # 7. implement the button function

    # implement button start
    def start(*args):
        cmd = 'python test.py --input_dir ./test_img --style Hosoda --gpu -1'
        os.system(cmd)

        file_path = "./test_output"
        save_path = "./store"
        path_dir = os.listdir(file_path)
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            from_path = os.path.join(file_path, filename)  # 旧文件的绝对路径(包含文件的后缀名)
            to_path = save_path  # 新文件的绝对路径
            copy(from_path, to_path)  # 完成复制黏贴

        path = "./test_img"
        path_dir = os.listdir(path)
        i = 0
        for filename in path_dir:  # 遍历pathDir下的所有文件filename
            i = i + 1
            full_path = os.path.join(path, filename)  # 文件的绝对路径(包含文件的后缀名)
            if(i > 0):
                os.remove(full_path)
        
        path = "./test_output"
        subprocess.call(["open", path])

    window.button_start.bind('<Button-1>', start)


    # implement button clear
    def display(*args):
        path = "./test_output"
        subprocess.call(["open", path])


    window.button_clear.bind('<Button-1>', display)


    # implement button upload
    def upload(*args):
        path = "./test_img"
        subprocess.call(["open", path])


    window.button_upload.bind('<Button-1>', upload)

    # 8. start GUI
    window.mainloop()

    acc = acc + 1





