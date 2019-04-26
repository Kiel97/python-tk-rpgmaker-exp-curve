import tkinter as tk

class Slider(tk.Frame):
    def __init__(self, label_text, from_=0, to_=100, master=None, variable=None):
        tk.Frame.__init__(self, master)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(1, weight=1)  

        self.grid()
        self.create_widgets(label_text, variable)

        self.slider["from_"] = from_
        self.slider["to"] = to_
        self.slider.set(round((from_+to_)/2))
    
    def create_widgets(self, label_text, variable):
        self.slider_label = tk.Label(self, text=label_text)
        self.slider = tk.Scale(self, orient=tk.HORIZONTAL, variable=variable)

        self.slider_label.grid(row=0, column=0)
        self.slider.grid(row=1, column=0, columnspan=2)