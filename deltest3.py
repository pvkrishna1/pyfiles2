class X:
    def __init__(self):
        print("in constuctor of x")
    def __del__(self):
        print("in destructor of x")
p=[X(),X(),X()]
del p[2]
del p
