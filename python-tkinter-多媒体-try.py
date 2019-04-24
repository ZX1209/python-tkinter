import tkinter as tk
from PIL import Image,ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        self.quitButton = tk.Button(self, text='show', command=self.showImage)
        self.quitButton.pack()
        
    def showImage(self):
        self.pilImage = Image.open("cat256ind.png")
        self.tkImage = ImageTk.PhotoImage(image=self.pilImage)
        self.label = tk.Label(self, image=self.tkImage)
        self.label.pack()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()