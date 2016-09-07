import threading
import led
# import beep

class myThread (threading.Thread):
    def __init__(self, name, func, params):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.params = params
    def run(self):
        print "Starting " + self.name
        self.func(self.params)
        print "Exiting " + self.name

def alarm():
    thread1 = myThread('ledThread', led.led, 3)
    # thread2 = myThread('beepThread', beep.beep)

    thread1.start()
    # thread2.start()
