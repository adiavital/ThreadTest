class Names(object):
    names_list=[]

    @staticmethod
    def names_list_add(name):
        Names.names_list.append(name)

    @staticmethod
    def names_list_display():
        print(Names.names_list)
