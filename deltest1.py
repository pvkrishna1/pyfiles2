class X:
    def __init__(self):
        print("in instructor of x")
    def __del__(self):
        print("in destructor of x")
x1=X()
print(x1)
del x1
