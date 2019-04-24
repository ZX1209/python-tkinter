from tkinter import ttk
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # root.geometry("800x600+10+10")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        img_gif = tk.PhotoImage(file = 'lena256ind.gif')
        label_img = tk.Label(root, image = img_gif)
        label_img.pack()


if __name__ == '__main__':
    root = tk.Tk()
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


