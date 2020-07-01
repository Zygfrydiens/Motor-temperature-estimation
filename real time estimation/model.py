import pickle
import pandas as pd
import bottleneck as bn

class Model:
    def __init__(self):
        self.file_name = 'generated.csv'
        self.MODEL_DIR = "C:/Users/Dester/PycharmProjects/motor/finalized_model.sav"
        self.df = {}
        self.time = []
        self.ambient = []
        self.coolant = []
        self.u_d = []
        self.u_q = []
        self.motor_speed = []
        self.i_d = []
        self.i_q = []
        self.profile_id = []
        self.pm = []
        self.x=1
        self.feature_col_names = ['ambient', 'coolant', 'u_d', 'u_q', 'motor_speed', 'i_d', 'i_q', 'profile_id']
        self.temp_model = pickle.load(open(self.MODEL_DIR, 'rb'))

    def load_data(self):
        self.df = pd.read_csv(self.file_name)
        self.time = self.df.index.values/2
        self.ambient = self.df["ambient"]
        self.coolant = self.df["coolant"]
        self.u_d = self.df["u_d"]
        self.u_q = self.df["u_q"]
        self.motor_speed = self.df["motor_speed"]
        self.i_d = self.df["i_d"]
        self.i_q = self.df["i_q"]
        self.profile_id = self.df["profile_id"]


    def estimate_temp(self):
        if len(self.time)>20:
            self.x = 10
        elif len(self.time)>50:
            self.x = 20
        elif len(self.time)>100:
            self.x = 100
        self.pm = bn.move_mean(self.temp_model.predict(self.df[self.feature_col_names].values), self.x, 1)
        self.data_list = [self.time, self.ambient, self.coolant, self.u_d, self.u_q, self.motor_speed, self.i_d,
                          self.i_q, self.pm]
    def clear_all(self):
        self.df.clear()
        self.time.clear()
        self.ambient.clear()
        self.coolant.clear()
        self.u_d.clear()
        self.u_q.clear()
        self.motor_speed.clear()
        self.i_d.clear()
        self.i_q.clear()
        self.profile_iq.clear()
        self.pm.clear()

#test = Model()
#test.load_data()
#test.estimate_temp()
#print(test.pm)
