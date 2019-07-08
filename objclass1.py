class X:
    def m1(self):
        print("in m1 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
print(X.__bases__)
print(Y.__bases__)
y1=Y()
print(y1)
p=y1.__hash__()
q=y1.__str__()
print(q)
print(p)
y1.m1()
y1.m2()
