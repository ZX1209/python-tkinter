from tkinter import ttk
import tkinter as tk

import pymysql

class table(tk.Frame):
    def __init__(self,root=None,size=(1,1)):
        super().__init__(root)
        rl,cl = size
        for ri in range(rl):
            for ci in range(cl):
                tmp = tk.Label(self)
                tmp['text'] = "something"
                tmp.grid(row=ri,column=ci)
        
        self.pack()



class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.host = "localhost"
        self.user = "gl"
        self.password = "glininin!"
        self.table = "tempdb"
        self.db = pymysql.connect(self.host,self.user,self.password,self.table);
        self.cursor = self.db.cursor()

        tmp = table(self,(2,2))
        tmp.pack()

        tmp = table(self,(3,3))
        tmp.pack(side=tk.LEFT)

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

        tree=ttk.Treeview(self)#表格
        column_names = ("No","Name","Sex","Birthday","Professor","DeptNo")
        tree["columns"]=column_names
        for column_name in column_names:
            tree.column(column_name,width=100)   #表示列,不显示
            tree.heading(column_name,text=column_name)

        
        # tree.heading("姓名",text="姓名-name")  #显示表头
        # tree.heading("年龄",text="年龄-age")
        # tree.heading("身高",text="身高-tall")
        # i = 0
        # for data in self.get_data():
        #     tree.insert("",i,values=data)
        #     i+=1
        
        self.db.close()
        
        tree.pack()


    def get_data(self):
        self.cursor.execute("select No,Name,Sex,Birthday,Professor,DeptNo from test")
        return self.cursor.fetchall()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("员工信息")
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
