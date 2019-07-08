class X:
    def __init__(self):
        print("in constructor of x")
    def display(self):
        print("welcome")
    def __del__(self):
        print("in destructor of x")
x1=X()
print(x1)
x1.display()
x1=X()
print(x1)
x1.display()
