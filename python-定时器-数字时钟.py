from tkinter import ttk
import tkinter as tk
from datetime import *
import threading

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        # root.geometry("800x600+10+10")
        self.pack()
        self.timeLabel = tk.Label(self)
        self.timeLabel['text'] = datetime.now().isoformat()
        self.timeLabel.pack()

        self.show_time()

    def show_time(self):
        self.timeLabel['text'] = datetime.now().isoformat()
        self.timeLabel.pack()

        t = threading.Timer(1,self.show_time)
        t.start()




if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root=root)
    app.mainloop()
