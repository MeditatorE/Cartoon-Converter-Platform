import tkinter
from Login import LoginWebPage


root = tkinter.Tk()


LoginButton = tkinter.Button(root, text="Log in/Sign up", command=LoginWebPage)
LoginButton.pack()


root.mainloop()








