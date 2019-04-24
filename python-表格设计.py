from tkinter import ttk
import tkinter as tk

import pymysql

class TableRow(tk.Frame):
    def __init__(self,root=None,colData=[]):
        super().__init__(root)
        for ci in range(len(colData)):
            tmp = tk.Label(self)
            tmp['text'] = "something"
            tmp.grid(row=1,column=ci)
    
        self.pack()

class Table(tk.Frame):
    def __init__(self,root=None,colnum=1):
        super().__init__(root)
        self.labels = []
        self.colnum=colnum
        self.pack()

    def updateView(self):
        for ri in range(len(self.labels)):
            for ci in range(self.colnum):
                self.labels[ri][ci].grid(row=ri,column=ci)
        self.pack()
            
        
    def insertData(self,colData=[]):
        try:
            self.labels.append(self.genCol(colData))
        except:
            pass

    def genCol(self,colDatas=[]):
        tmpCol = []
        if len(colDatas)!=self.colnum:
            raise RuntimeError("something wrong")
        
        if colDatas:
            for colData in colDatas:
                tmpCol.append(tk.Label(self,text=colData))
        return tmpCol

        





class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.table = Table(self,3)
        self.updateButton = tk.Button(self)
        self.updateButton['text'] = "更新"
        self.updateButton['command'] = self.bind
        self.updateButton.pack()

    def bind(self):
        self.table.insertData(['1','2','3'])
        self.table.updateView()

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
