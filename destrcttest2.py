class X:
    def __init__(self):
        print("in constructor of x")
    def display(self):
        print("welcome")
    def __del__(self):
        print("in destructor of x")
X().display()
