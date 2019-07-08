class X:
    def m1(self):
        print("in no param m1 of x")
    def m1(self,a):
        print("in one param of x")
    def m1(self,a,b):
        print("in 2 param of x")
x1=X()
x1.m1(1000,2000)
