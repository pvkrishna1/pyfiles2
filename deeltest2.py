class Emp:
    """"emp app"""
    empcnt=0
    def __init__(self,eid,ename,eadd,esal):
        self.eid=eid
        self.ename=ename
        self.eadd=eadd
        self.esal=esal
        Emp.empcnt=Emp.empcnt+1
    def __del__(self):
        Emp.empcnt=Emp.empcnt-1
e1=Emp(7788,"scott","dallas",3000.00)
e2=Emp(7920,"smith","mumbai",4000.00)
e3=Emp(7369,"blake","hennai",3500.00)
del e2
print("total no.of employees are:",Emp.empcnt)
