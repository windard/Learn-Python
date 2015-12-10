import threading

class ThreadClass(threading.Thread):
    def run(self):
        er = self.getName()
        print("Hello,I'm %s"%er)

for i in range(4):
    t = ThreadClass()
    t.start()