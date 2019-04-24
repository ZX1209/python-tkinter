import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # 變量定義
        self.opr = OracleOpr()
        self.list = self.init_data()
        self.item_selection = ''
        self.data = []

        # 定義區域，把全局分為上中下三部分
        self.frame_top = tk.Frame(width=600, height=90)
        self.frame_center = tk.Frame(width=600, height=180)
        self.frame_bottom = tk.Frame(width=600, height=90)

        # 定義上部分區域
        self.lb_tip = tk.Label(self.frame_top, text="評議小組名稱")
        self.string = tk.StringVar()
        self.string.set('')
        self.ent_find_name = tk.Entry(self.frame_top, textvariable=self.string)
        self.btn_query = tk.Button(self.frame_top, text="查詢", command=self.query)
        self.lb_tip.grid(row=0, column=0, padx=15, pady=30)
        self.ent_find_name.grid(row=0, column=1, padx=45, pady=30)
        self.btn_query.grid(row=0, column=2, padx=45, pady=30)

        # 定義下部分區域
        self.btn_delete = tk.Button(self.frame_bottom, text="刪除", command=self.delete)
        self.btn_update = tk.Button(self.frame_bottom, text="修改", command=self.update)
        self.btn_add = tk.Button(self.frame_bottom, text="添加", command=self.add)
        self.btn_delete.grid(row=0, column=0, padx=20, pady=30)
        self.btn_update.grid(row=0, column=1, padx=120, pady=30)
        self.btn_add.grid(row=0, column=2, padx=30, pady=30)

        # 定義中心列表區域
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=("a", "b", "c", "d"))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=tk.VERTICAL, command=self.tree.yview)
        # 定義樹形結構與滾動條
        self.tree.configure(yscrollcommand=self.vbar.set)
        # 表格的標題
        self.tree.column("a", width=80, anchor="center")
        self.tree.column("b", width=120, anchor="center")
        self.tree.column("c", width=120, anchor="center")
        self.tree.column("d", width=120, anchor="center")
        self.tree.heading("a", text="小組編號")
        self.tree.heading("b", text="小組名稱")
        self.tree.heading("c", text="負責人")
        self.tree.heading("d", text="聯繫方式")
        # 調用方法獲取表格內容插入及樹基本屬性設置
        self.tree["selectmode"] = "browse"
        self.get_tree()self.tree.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10)
        
        self.vbar.grid(row=0, column=1, sticky=tk.NS)

        # 定義整體區域
        self.frame_top.grid(row=0, column=0, padx=60)
        self.frame_center.grid(row=1, column=0, padx=60, ipady=1)
        self.frame_bottom.grid(row=2, column=0, padx=60)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        # 窗體設置
        self.center_window(600, 360)
        self.title('評議小組管理')
        self.resizable(False, False)
        self.mainloop()

    # 窗體居中
    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        # 寬高及寬高的初始點座標
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)

    # 數據初始化獲取
    def init_data(self):
        result, _ = self.opr.query()
        if self.opr.queryStatus:
            return 0
        else:
            return result

    # 表格內容插入
    def get_tree(self):
        if self.list == 0:
            tkinter.messagebox.showinfo("錯誤提示", "數據獲取失敗")
        else:
            # 刪除原節點
            for _ in map(self.tree.delete, self.tree.get_children("")):
                pass
            # 更新插入新節點
            for i in range(len(self.list)):
                group = self.list[i]
                self.tree.insert("", "end", values=(group[0],
                                                    group[1],
                                                    group[2],
                                                    group[3]), text=group[0])
            # TODO 此處需解決因主進程自動刷新引起的列表項選中後重置的情況，我採用的折中方法是：把選中時的數據保存下來，作為記錄

            # 綁定列表項單擊事件
            self.tree.bind("<ButtonRelease-1>", self.tree_item_click)
            self.tree.after(500, self.get_tree)

    # 單擊查詢按鈕觸發的事件方法
    def query(self):
        query_info = self.ent_find_name.get()
        self.string.set('')
        # print(query_info)
        if query_info is None or query_info == '':
            tkinter.messagebox.showinfo("警告", "查詢條件不能為空！")
            self.get_tree()
        else:
            result, _ = self.opr.query(queryby="where name like '%" + query_info + "%'")
            self.get_tree()
            if self.opr.queryStatus:
                tkinter.messagebox.showinfo("警告", "查詢出錯，請檢查數據庫服務是否正常")
            elif not result:
                tkinter.messagebox.showinfo("查詢結果", "該查詢條件沒有匹配項！")
            else:
                self.list = result
                # TODO 此處需要解決彈框後代碼列表刷新無法執行的問題

    # 單擊刪除按鈕觸發的事件方法
    def delete(self):
        # if self.item_selection is None or self.item_selection == '':
        #     tkinter.messagebox.showinfo("刪除警告", "未選中待刪除值")
        # else:
        #     # TODO： 刪除提示
        #     self.opr.delete(deleteby="no = '"+self.item_selection+"'")
        #     if self.opr.deleteStatus:
        #         tkinter.messagebox.showinfo("刪除警告", "刪除異常，可能是數據庫服務意外關閉了。。。")
        #     else:
        #         self.list = self.init_data()
        #         self.get_tree()
        pass

    # 為解決窗體自動刷新的問題，記錄下單擊項的內容
    def tree_item_click(self, event):
        try:
            selection = self.tree.selection()[0]
            self.data = self.tree.item(selection, "values")
            self.item_selection = self.data[0]
        except IndexError:
            tkinter.messagebox.showinfo("單擊警告", "單擊結果範圍異常，請重新選擇！")

    # 單擊更新按鈕觸發的事件方法
    def update(self):
        if self.item_selection is None or self.item_selection == '':
            tkinter.messagebox.showinfo("更新警告", "未選中待更新項")
        else:
            data = [self.item_selection]
            self.data = self.set_info(2)
            if self.data is None or not self.data:
                return
            # 更改參數
            data = data + self.data
            self.opr.update(updatelist=data)
            if self.opr.insertStatus:
                tkinter.messagebox.showinfo("更新小組信息警告", "數據異常庫連接異常，可能是服務關閉啦~")
            # 更新界面，刷新數據
            self.list = self.init_data()
            self.get_tree()

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

    # 此方法調用彈窗傳遞參數，並返回彈窗的結果
    def set_info(self, dia_type):
        """
        :param dia_type:表示打開的是添加窗口還是更新窗口，添加則參數為1，其餘參數為更新
        :return: 返回用户填寫的數據內容，出現異常則為None
        """
        dialog = MyDialog(data=self.data, dia_type=dia_type)
        # self.withdraw()
        self.wait_window(dialog)  # 這一句很重要！！！
        return dialog.group_info


# 添加窗口或者更新窗口
class MyDialog(tk.Toplevel):
    def __init__(self, data, dia_type):
        super().__init__()

        # 窗口初始化設置，設置大小，置頂等
        self.center_window(600, 360)
        self.wm_attributes("-topmost", 1)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.donothing)   # 此語句用於捕獲關閉窗口事件，用一個空方法禁止其窗口關閉。

        # 根據參數類別進行初始化
        if dia_type == 1:
            self.title('添加小組信息')
        else:
            self.title('更新小組信息')

        # 數據變量定義
        self.no = tk.StringVar()
        self.name = tk.StringVar()
        self.pname = tk.StringVar()
        self.pnum = tk.StringVar()
        if not data or dia_type == 1:
            self.no.set('')
            self.name.set('')
            self.pname.set('')
            self.pnum.set('')
        else:
            self.no.set(data[0])
            self.name.set(data[1])
            self.pname.set(data[2])
            self.pnum.set(data[3])

        # 錯誤提示定義
        self.text_error_no = tk.StringVar()
        self.text_error_name = tk.StringVar()
        self.text_error_pname = tk.StringVar()
        self.text_error_pnum = tk.StringVar()
        self.error_null = '該項內容不能為空!'
        self.error_exsit = '該小組編號已存在!'

        self.group_info = []
        # 彈窗界面佈局
        self.setup_ui()

    # 窗體佈局設置
    def setup_ui(self):
        # 第一行（兩列）
        row1 = tk.Frame(self)
        row1.grid(row=0, column=0, padx=160, pady=20)
        tk.Label(row1, text='小組編號：', width=8).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.no, width=20).pack(side=tk.LEFT)
        tk.Label(row1, textvariable=self.text_error_no, width=20, fg='red').pack(side=tk.LEFT)
        # 第二行
        row2 = tk.Frame(self)
        row2.grid(row=1, column=0, padx=160, pady=20)
        tk.Label(row2, text='小組名稱：', width=8).pack(side=tk.LEFT)
        tk.Entry(row2, textvariable=self.name, width=20).pack(side=tk.LEFT)
        tk.Label(row2, textvariable=self.text_error_name, width=20, fg='red').pack(side=tk.LEFT)
        # 第三行
        row3 = tk.Frame(self)
        row3.grid(row=2, column=0, padx=160, pady=20)
        tk.Label(row3, text='負責人姓名：', width=10).pack(side=tk.LEFT)
        tk.Entry(row3, textvariable=self.pname, width=18).pack(side=tk.LEFT)
        tk.Label(row3, textvariable=self.text_error_pname, width=20, fg='red').pack(side=tk.LEFT)
        # 第四行
        row4 = tk.Frame(self)
        row4.grid(row=3, column=0, padx=160, pady=20)
        tk.Label(row4, text='手機號碼：', width=8).pack(side=tk.LEFT)
        tk.Entry(row4, textvariable=self.pnum, width=20).pack(side=tk.LEFT)
        tk.Label(row4, textvariable=self.text_error_pnum, width=20, fg='red').pack(side=tk.LEFT)
        # 第五行
        row5 = tk.Frame(self)
        row5.grid(row=4, column=0, padx=160, pady=20)
        tk.Button(row5, text="取消", command=self.cancel).grid(row=0, column=0, padx=60)
        tk.Button(row5, text="確定", command=self.ok).grid(row=0, column=1, padx=60)

    def center_window(self, width, height):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(size)

    # 點擊確認按鈕綁定事件方法
    def ok(self):

        self.group_info = [self.no.get(), self.name.get(), self.pname.get(), self.pnum.get()]  # 設置數據
        if self.check_info() == 1:  # 進行數據校驗，失敗則不關閉窗口
            return
        self.destroy()  # 銷燬窗口

    # 點擊取消按鈕綁定事件方法
    def cancel(self):
        self.group_info = None  # 空！
        self.destroy()

    # 數據校驗和用户友好性提示，校驗失敗返回1，成功返回0
    def check_info(self):
        is_null = 0
        str_tmp = self.group_info
        if str_tmp[0] == '':
            self.text_error_no.set(self.error_null)
            is_null = 1
        if str_tmp[1] == '':
            self.text_error_name.set(self.error_null)
            is_null = 1
        if str_tmp[2] == '':
            self.text_error_pname.set(self.error_null)
            is_null = 1
        if str_tmp[3] == '':
            self.text_error_pnum.set(self.error_null)
            is_null = 1

        if is_null == 1:
            return 1
        res, _ = OracleOpr().query(queryby="where no = '"+str_tmp[0]+"'")
        print(res)
        if res:
            self.text_error_no.set(self.error_exsit)
            return 1
        return 0

    # 空函數
    def donothing(self):
        pass
