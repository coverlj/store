class jsq:
    N=0.0
    def add(self,num1):
        self.N=self.N+num1
        return self.N
    def jf(self,num1):
        self.N=self.N-num1
        return self.N
    def cf(self,num1):
        self.N=self.N*num1
        return self.N
    def cuf(self,num1):
        self.N = self.N/num1
        return self.N
    def qc(self):
        self.N=0.0

d=jsq()
print("欢迎使用AAA版计算器")
d.N=float(input("请输入第一个数："))
while True:
    ff=input("请输入计算方法(+、-、*、/、AC)退出按F：")
    if ff == "AC":
        d.qc()
        d.N = float(input("请输入第一个数："))
        continue
    if ff=="F":
        break
    b=float(input("请输入第二个数："))
    if ff=="+":
        print("结果等于",d.add(b))
    elif ff=="-":
        print("结果等于",d.jf(b))
    elif ff=="*":
        print("结果等于",d.cf(b))
    elif ff=="/":
        print("结果等于",d.cuf(b))







