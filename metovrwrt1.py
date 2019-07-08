class X:
    def m1(self):
        print("in m1 of X")
    def m2(self):
        print("in m2 of X")
class Y(X):
    def m3(self):
        print("in m3 of Y")
    def m2(self):
        print("in m2 of Y")
y1=Y()
y1.m1()
y1.m2()
y1.m3()
x1=X()
x1.m1()
x1.m2()
