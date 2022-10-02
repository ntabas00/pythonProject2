import threading
class MyThreadClass(threading.Thread):
    def __init__(self) :
      super(MyThreadClass, self).__init__()
    def run(self):
       c=0
       while(c<15):
            c=c+1
            print ("Thread finished ")


def f():
    c=0
    while(c<15):
        c=c+1
        print("Thread Started")

myThreadFunc = threading.Thread(target=f)
myThreadObj=MyThreadClass()
myThreadFunc.start()
myThreadObj.start()
myThreadFunc.join()
myThreadObj.join()
