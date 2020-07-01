from view import *
from model import *
from tkinter import *
from pubsub import *

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model()
        self.view = View(parent)
        self.view.setup()
        print("Controller running")

        pub.subscribe(self.start_button_pressed, "Start/Stop button pressed")

    def start_button_pressed(self):
        print("controller - start button pressed")
        self.model.load_data()
        self.model.estimate_temp()
        for cnt, plot in enumerate(self.view.plot_list):
            self.view.plot(self.view.plot_list[cnt][0], self.view.plot_list[cnt][1], self.model.data_list[0],
                           self.model.data_list[cnt+1], self.view.plot_list[cnt][2], self.view.plot_list[cnt][3])
            print(self.view.plot_list[cnt][0])





if __name__ == "__main__":
    root = Tk()
    app = Controller(root)
    root.mainloop()
