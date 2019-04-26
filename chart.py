"""Chart - a module containing custom class displaying plot on canvas in Tk application.
    It uses matplotlib and tkinter."""
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

class Chart(tk.Frame):
    """A customized tkinter.Frame displaying plot on canvas in Tk application."""
    def __init__(self, master=None, xlabel_text='Level', ylabel_text='Total Exp'):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets(xlabel_text, ylabel_text)

    def create_widgets(self, xlabel_text, ylabel_text):
        """Method creating UI, passed arguments are set as Plot axis descriptions."""
        self.figure = Figure()

        self.chart = self.figure.add_subplot(111)
        self.chart.set_xlabel(xlabel_text)
        self.chart.set_ylabel(ylabel_text)
        self.chart.set_xlim([1, 99])

        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.draw()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def redraw_chart(self, x_list, y_list):
        """Clears plot and inserts points on plot."""
        self.chart.clear()
        self.chart.plot(x_list, y_list, 'b^')
