class X:
    a=1000
    def m1(self):
        print("in m1 of X")
class Y(X):
    c=3000
    def __init__(self):
        self.d=4000
    def m2(self):
        print("in m2 of y")
y1=Y()
print(Y.a)
print(Y.c)
print(y1.d)
y1.m1()
y1.m2()
