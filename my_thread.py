import threading
from dal import select_data
from name_parser import parser_process
from helper import tuple_to_list


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, threadLock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.threadLock = threadLock
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        self.threadLock.acquire()
        my_tuple = select_data()
        if my_tuple is not ():
            my_list = tuple_to_list(my_tuple)
            parser_process(my_list)
            # Free lock to release next thread
            self.threadLock.release()

