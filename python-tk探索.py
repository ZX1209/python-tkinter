import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import pymysql



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        

        # 数据库
        self.host = "localhost"
        self.user = "gl"
        self.password = "glininin!"
        self.table = "tempdb"
        self.db = pymysql.connect(self.host,self.user,self.password,self.table);
        self.cursor = self.db.cursor()

        self.datas = self.get_all_data()


        self.frame_top = tk.Frame(width=600,height=90)
        self.frame_center = tk.Frame(width=600,height=270)

        # 上半部分
        self.addButton = tk.Button(self.frame_top,text="添加")
        self.addButton['command'] = self.get_tree
        self.addButton.grid(row=0,column=0)

        self.updateButton = tk.Button(self.frame_top,text="修改")
        self.updateButton.grid(row=0,column=1)

        self.delButton = tk.Button(self.frame_top,text="删除")
        self.delButton['command'] = self.drop_tree
        self.delButton.grid(row=0,column=2)

        self.frame_top.grid(row=0,column=0)

        # 中心部分
        self.column_names = ("No","Name","Sex","Birthday","Professor","DeptNo")
        self.tree = ttk.Treeview(self.frame_center,show="headings",height=8,columns=self.column_names)
        
        for column_name in self.column_names:
            self.tree.column(column_name,width=80,anchor="center")
            self.tree.heading(column_name,text=column_name)
        self.tree["selectmode"] = "browse"
        self.get_tree()
        self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)

        # 定义整体区域
        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_top.configure(background='black')


        self.configure(background='black')
        self.mainloop()

        self.db.close()

    def get_tree(self):
        for i in range(len(self.datas)):
            group = self.datas[i]
            
            self.tree.insert("","end",values=group, text=group[0])
    def drop_tree(self):
        # 刪除原節點
        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass

    def get_all_data(self):
        self.cursor.execute("select No,Name,Sex,Birthday,Professor,DeptNo from test")
        return self.cursor.fetchall()


    def set_info(self, dia_type):
        """
        :param dia_type:表示打開的是添加窗口還是更新窗口，添加則參數為1，其餘參數為更新
        :return: 返回用户填寫的數據內容，出現異常則為None
        """
        dialog = MyDialog(data=self.data, dia_type=dia_type)
        # self.withdraw()
        self.wait_window(dialog)  # 這一句很重要！！！
        return dialog.group_info
    
    # 單擊添加按鈕觸發的事件方法
    def add(self):
        # 接收彈窗的數據
        self.data = self.set_info(1)
        if self.data is None or not self.data:
            return
        # 更改參數
        self.opr.insert(insertlist=self.data)
        if self.opr.insertStatus:
            tkinter.messagebox.showinfo("添加小組信息警告", "數據異常庫連接異常，可能是服務關閉啦~")
        # 更新界面，刷新數據
        self.list = self.init_data()
        self.get_tree()

class MyDialog(tk.Toplevel):
    def __init__(self, data, dia_type):
        super().__init__()

        # 窗口初始化設置，設置大小，置頂等
        self.center_window(600, 360)
        self.wm_attributes("-topmost", 1)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.donothing)   # 此語句用於捕獲關閉窗口事件，用一個空方法禁止其窗口關閉。


if __name__=="__main__":
    app = MainWindow()