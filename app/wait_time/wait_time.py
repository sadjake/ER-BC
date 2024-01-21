import random
import datetime

class WaitTime():
    def __init__(self, hosp_id, hospital_name, wait_time):
        self._id = hosp_id
        self._hospital_name = hospital_name
        self._wait_time = wait_time
    
    def update_wait_time(self):
        # true: add; false: subtract
        add_subtract = random.choice([True, False])
        delta_time = random.randint(1, 5)
        if add_subtract or (self._wait_time - delta_time) < 0:
            self._wait_time += delta_time
        else:
            self._wait_time -= random.randint(1, 5)

    def get_id(self):
        return self._id

    def get_wait_time(self):
        return self._wait_time
    
    def get_hospital_name(self):
        return self._hospital_name
    
    def get_data(self):
        hospital_name = self.get_hospital_name()
        self.update_wait_time()
        wait_time = self.get_wait_time()
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "name": hospital_name,
            "wait_time": wait_time,
            "date": date
        }
