import pandas as pd
import csv
import time


class DataGen:
    def __init__(self):
        self.i = 0
        self.DATA_DIR = "C:/Users/Dester/PycharmProjects/motor/data/pmsm_temperature_data.csv"
        self.df = pd.read_csv(self.DATA_DIR)
        self.feature_col_names = ['ambient', 'coolant', 'u_d', 'u_q', 'motor_speed', 'i_d', 'i_q', 'profile_id' ]
        self.is_started = False

    def start(self):
        self.is_started = not self.is_started
        print("Is simulation started: " + str(self.is_started))

    def generate_data(self):
        with open('generated.csv', 'w') as csv_file:
            self.csv_writer = csv.DictWriter(csv_file, fieldnames=self.feature_col_names)
            self.csv_writer.writeheader()

        while True:
            with open('generated.csv', 'a') as csv_file:
                self.csv_writer = csv.DictWriter(csv_file, fieldnames=self.feature_col_names)

                info = {
                    'ambient': self.df["ambient"][self.i],
                    'coolant': self.df["coolant"][self.i],
                    'u_d' : self.df["u_d"][self.i],
                    'u_q' : self.df["u_q"][self.i],
                    'motor_speed' : self.df["motor_speed"][self.i],
                    'i_d' : self.df["i_d"][self.i],
                    'i_q' : self.df["i_q"][self.i],
                    'profile_id' : self.df["profile_id"][self.i]
                    }

                self.csv_writer.writerow(info)
                print(self.i, self.df["ambient"][self.i], self.df["coolant"][self.i], self.df["u_d"][self.i],
                      self.df["u_q"][self.i], self.df["motor_speed"][self.i], self.df["i_d"][self.i],
                      self.df["i_q"][self.i], self.df["profile_id"][self.i])

                self.i += 1
            time.sleep(0.001)

data_gen = DataGen()
data_gen.start()
data_gen.generate_data()
