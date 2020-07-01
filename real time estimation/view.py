from tkinter import *
from pubsub import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib import *
import matplotlib.animation as animation
from matplotlib import style

class View:
    def __init__(self, parent):
        self.root = parent
        self.root.resizable(False, False)
        self.font = {'family': 'normal',
                'weight': 'normal',
                'size': 8}

        rc('font', **self.font)


    def setup(self):
        self.create_widgets()
        self.setup_layout()
        self.plot_list =[["Ambient temperature", "Temperature [-]", self.f1, self.ambient_figure],
                         ["Coolant temperature", "Temperature [-]", self.f2, self.coolant_figure],
                         ["Motor speed", "Speed [-]", self.f3, self.motor_speed_figure],
                         ["D-axis current", "Current [-]", self.f4, self.i_d_figure],
                         ["Q-axis current", "Current [-]", self.f5, self.i_q_figure],
                         ["D-axis voltage", "Voltage [-]", self.f6, self.u_d_figure],
                         ["Q-axis voltage", "Voltage [-]", self.f7, self.u_q_figure],
                         ["Motor temperature \n estimation", "Temperature", self.f8, self.pm_figure]]

    def start(self):
        pub.sendMessage("Start/Stop button pressed")
        print("View - start button pressed")

    def create_widgets(self):
        self.button_start = Button(self.root, text="Start", command=self.start)
        self.button_start.config(width=5, height=2)

        self.f1 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f2 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f3 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f4 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f5 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f6 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f7 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f8 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)
        self.f9 = Frame(self.root, highlightbackground="#a5a5ad", highlightthickness=1, width=200, height=200)

        self.ambient_figure = Figure(figsize=(3, 3), dpi=80)
        self.coolant_figure = Figure(figsize=(3, 3), dpi=80)
        self.motor_speed_figure = Figure(figsize=(3, 3), dpi=80)
        self.i_d_figure = Figure(figsize=(3, 3), dpi=80)
        self.i_q_figure = Figure(figsize=(3, 3), dpi=80)
        self.u_d_figure = Figure(figsize=(3, 3), dpi=80)
        self.u_q_figure = Figure(figsize=(3, 3), dpi=80)
        self.pm_figure = Figure(figsize=(3, 3), dpi=80)

    def setup_layout(self):
        # button
        self.button_start.grid(row=0, column=1)
        # frames
        self.f1.grid(row=1, column=0)
        self.f2.grid(row=1, column=1)
        self.f3.grid(row=1, column=2)
        self.f4.grid(row=2, column=0)
        self.f5.grid(row=2, column=1)
        self.f6.grid(row=2, column=2)
        self.f7.grid(row=3, column=0)
        self.f8.grid(row=3, column=1)
        self.f9.grid(row=3, column=2)

    def plot(self, title, y_label, x, y, frame, figure):
        #self.ax = figure.add_subplot(111)
        self.ax = figure.add_axes([0.2, 0.2, 0.7, 0.7])
        self.ax.clear()
        self.ax.set_title(title)
        self.ax.set_xlabel("Time [s]")
        self.ax.set_ylabel(y_label)
        self.ax.grid(which='minor', color='#CCCCCC', linestyle=':')
        self.ax.grid(linestyle='-', linewidth=1)
        self.ax.plot(x, y)
        self.canvas = FigureCanvasTkAgg(figure, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)


# Testing
if __name__ == "__main__":
    print("running view")
    root = Tk()
    view = View(root)
    view.setup()
    root.mainloop()