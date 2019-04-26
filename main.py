import tkinter as tk

from sliders import Sliders
from charts import Charts
from formula import get_exp_for_next_level_list
from formula import get_total_exp_list

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.charts = Charts(self)
        self.charts.grid(row=0)

        self.sliders = Sliders(self)
        self.sliders.grid(row=1)

        self.quit_btn = tk.Button(self, text="OK", command=self.quit)
        self.quit_btn.grid(row=2, columnspan=2)
    
    def on_slider_value_changed(self, base, extra, accA, accB):
        total_exp_list = get_total_exp_list(from_=1, to_=99, base_value=base, extra_value=extra, acceleration_A=accA, acceleration_B=accB)
        exp_per_lvl_list = get_exp_for_next_level_list(from_=1, to_=99, base_value=base, extra_value=extra, acceleration_A=accA, acceleration_B=accB)
        
        self.charts.on_slider_value_changed(total_exp_list, exp_per_lvl_list)

tk_ = tk.Tk()
app = Application(tk_)
tk_.title('EXP Curve')
tk_.resizable(width=False, height=False)
tk_.mainloop()