class X:
    def m1(self):
        print("in no param of x")
    def m1(self,a,b):
        print("in two param of x")
    def m1(self,a):
        print("in one param of x")
x1=X()
x1.m1(1000)
x1.m1(123,456)
