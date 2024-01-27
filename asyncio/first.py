#%%
import time
import threading 

class Mayhem(threading.Thread):
    def __init__(self, map):
        super().__init__()
        self.map = map
    
    def run(self):
        for key, value in self.map.items():
            print(key, value)
            time.sleep(value ** 2)

mapping = {"key1": 1, "key2": 2, "key3": 3}
thread = Mayhem(mapping)
thread.start()
        