import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self):
        self.core = tk.Tk()
        self.core.geometry("538x400")
        self.header = tk.Frame(self.core, bg="gray2")
        self.header.grid(row=0, column=0)
        self.title = tk.Label(self.header, text="WEB SCRAPPER", font="Arial 12", fg="green2", bg="gray2")
        self.title.grid(row=0, column=0, sticky="WE", columnspan=2, ipadx=(400 - self.title.winfo_x()) / 2)
        self.parameter01_label = tk.Label(self.core, text="Parameter 1", font="Arial 10", fg="green2", bg="gray2")
        self.parameter01_label.grid(row=1, column=0, sticky="W")
        self.parameter01 = tk.Entry(self.core, width=10, bg="blue")
        self.parameter01.grid(row=1, column=1, sticky="W")

        #self.table = ttk.Treeview(self.core, show="headings", columns=('Product', 'Price'))
        #self.table.grid(row=2, column=0, columnspan=4)
        #self.table.column('Product', anchor="center", width=200)
        #self.table.heading('Product', text="Product")
        #self.table.column('Price', anchor="center", width=100)
        #self.table.heading('Price', text="Price")

    def unpack_data(self):
        pass

    def run(self):
        self.core.mainloop()


gui = MainWindow()
gui.run()
