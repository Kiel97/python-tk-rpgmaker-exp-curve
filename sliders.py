import tkinter as tk
from slider import Slider

class Sliders(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.bind_sliders()
        self.on_slider_value_changed(None)
    
    def create_widgets(self):
        self.base_var = tk.IntVar()
        self.base_slider = Slider("Base Value", from_=10, to_=50, master=self, variable=self.base_var)
        self.base_slider.grid(row=0, column=0)

        self.extra_var = tk.IntVar()
        self.extra_slider = Slider("Extra Value", from_=0, to_=40, master=self, variable=self.extra_var)
        self.extra_slider.grid(row=0, column=1)

        self.accA_var = tk.IntVar()
        self.accA_slider = Slider("Acceleration A", from_=10, to_=50, master=self, variable=self.accA_var)
        self.accA_slider.grid(row=1, column=0)

        self.accB_var = tk.IntVar()
        self.accB_slider = Slider("Acceleration B", from_=10, to_=50, master=self, variable=self.accB_var)
        self.accB_slider.grid(row=1, column=1)

    def bind_sliders(self):
        self.base_slider.slider.bind('<ButtonRelease-1>', self.on_slider_value_changed)
        self.extra_slider.slider.bind('<ButtonRelease-1>', self.on_slider_value_changed)
        self.accA_slider.slider.bind('<ButtonRelease-1>', self.on_slider_value_changed)
        self.accB_slider.slider.bind('<ButtonRelease-1>', self.on_slider_value_changed)
    
    def on_slider_value_changed(self, event):
        base = self.base_var.get()
        extra = self.extra_var.get()
        accA = self.accA_var.get()
        accB = self.accB_var.get()

        if self.master:
            self.master.on_slider_value_changed(base, extra, accA, accB)