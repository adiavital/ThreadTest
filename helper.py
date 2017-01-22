from dal import select_data
from dal import select_data
from name_parser import parser_process
import time
import multiprocessing


def tuple_to_list(my_tuple):
    my_list = [list(x) for x in my_tuple]
    return my_list


def procces_seq():
    my_tuple = select_data()
    if my_tuple is not ():
        my_list = tuple_to_list(my_tuple)
        parser_process(my_list)
