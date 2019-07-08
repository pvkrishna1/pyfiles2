class cust:
    """cust app"""
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def __str__(self):
        return self.cname+" "+self.cadd+" "+str(self.cacno)+" "+str(self.cbal)+" "+cust.cbname
    def deposit(self,dmat):
        self.cbal=self.cbal+dmat
    def withdraw(self,wmat):
        self.cbal=self.cbal-wmat
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
c1=cust("ravana","srilanka",1001,100000.0)
c2=cust("sita","india",1002,20000.0)
c3=cust("trumph","US",1003,70000.0)
x=[c1,c2,c3]
for p in x:
    print(p)
print("after sorting")
x.sort(key=lambda c:cbal,reverse=False)
for q in x:
    print(q)
