import tkinter as tk
from tkinter import ttk

from chart import Chart

class Charts(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.xlist = list(range(1,100))
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.tabs = ttk.Notebook(self, width=600, height=450)
        self.tabs.grid()

        self.total_exp_page = tk.Frame(self.tabs)
        self.exp_per_lvl_page = tk.Frame(self.tabs)

        self.total_exp_chart = Chart(self.total_exp_page)
        self.exp_per_lvl_chart = Chart(self.exp_per_lvl_page, ylabel_text='Exp Per Level')

        self.total_exp_chart.pack(fill=tk.BOTH)
        self.exp_per_lvl_chart.pack(fill=tk.BOTH)

        self.tabs.add(self.total_exp_page, text="Total Exp")
        self.tabs.add(self.exp_per_lvl_page, text="Exp Level")
        self.tabs.grid()
    
    def on_slider_value_changed(self, total_exp_list, exp_per_lvl_list):
        
        self.total_exp_chart.redraw_chart(self.xlist, total_exp_list)
        self.exp_per_lvl_chart.redraw_chart(self.xlist, exp_per_lvl_list)