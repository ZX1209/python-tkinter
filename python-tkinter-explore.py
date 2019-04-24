from tkinter import ttk
import tkinter as tk

intext = "test"

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # root.geometry("800x600+10+10")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

        self.input = tk.Entry(self)
        self.input['width'] = 100
        self.input.pack()

        self.button = tk.Button(self)
        self.button['text'] = "click me"
        self.button['command'] = self.show_text
        self.button.pack()

        self.button = tk.Button(self)
        self.button['text'] = "lavel me"
        self.button['command'] = self.add_label
        self.button.pack()

    def show_text(self):
        line = text
        print(line)

    def say_hi(self):
        print("hi there, everyone!")
    def add_label(self):
        self.tmp = tk.Label(self)
        self.tmp['text'] = intext
        self.tmp.pack()
    def show_msg(self):
        tk.tkMessageBox('msg')

root = tk.Tk()

style = ttk.Style()
print(style.theme_names()) 
style.theme_use('clam') 

app = Application(root=root)
app.mainloop()

# class MyApplication(tk.frame):



# root = tk.Tk()
# root.geometry("800x600+10+10")

# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = tk.Listbox(root)          #  创建两个列表组件
# listb2 = tk.Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
 
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
 
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()                 # 进入消息循环
