from dal import update_data, update_name
from names import Names


def processed_mark(user_id):
    update_data(user_id)

def change_name(name):
    if len(name) > 3:
        new_name = str(name[::-1])
    else:
        new_name = name + 'ing'
    return new_name

def parser_process(lst):
    for item in lst:
        processed_mark(item[1])
        new_name = str(change_name(item[0]))
        update_name(new_name, item[1])
        print("done changing %s to %s" % (item[0], new_name))

