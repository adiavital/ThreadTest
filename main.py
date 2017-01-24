from dal import select_data
from name_parser import parser_process
# from helper import tuple_to_list, select_data_process , procces_seq
from helper import procces_seq , tuple_to_list
import time
import multiprocessing
import threading
from my_thread import myThread
import time

t1 = time.time()
threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1, threadLock)
thread2 = myThread(2, "Thread-2", 2, threadLock)

# Start new Threads
thread1.start()
thread2.start()

# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)

# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print ("Exiting Main Thread")
thread1.join()
thread2.join()

print(time.time()-t1)





# if __name__ == "__main__":
#     t1 = time.time()
#     # pro1 = multiprocessing.Process(target=procces_seq)
#     # pro2 = multiprocessing.Process(target=procces_seq)
#     pro1 = threading.Thread(target=procces_seq)
#     pro2 = threading.Thread(target=procces_seq)
#
#     # pro3 = multiprocessing.Process(target=procces_seq)
#     pro1.start()
#     # time.sleep(0.7)
#     pro2.start()
#     # time.sleep(0.7)
#     # pro3.start()
#     pro1.join()
#     pro2.join()
#     # pro3.join()
#     print (time.time() - t1)



# if __name__ == "__main__":
#     t1 = time.time()
#     for i in range(0,2):
#         my_tuple = select_data()
#         if my_tuple is not ():
#             my_list = tuple_to_list(my_tuple)
#             parser_process(my_list)
#     print(time.time() - t1)
