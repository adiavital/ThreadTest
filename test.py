class Girls(object):
    names=[]

    @staticmethod
    def girls_append(name):
        Girls.names.append(name)

    @staticmethod
    def girls_print():
        print(Girls.names)

# a = Girls()
# a.girls_append('dana')
# a.girls_print()
# b = Girls()
# b.girls_append('adi')
# b.girls_print()
# Girls.girls_append('bla')
# Girls.girls_print()
# Girls().girls_append('koko')
# Girls().girls_print()


for i in range(5):
    Girls.girls_append('bla')
    Girls.girls_print()

for i in range(5):
    Girls.girls_append('bla')
    Girls.girls_print()
