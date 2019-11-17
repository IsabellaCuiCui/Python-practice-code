#本例用于试验类初始化有无的区别
#带__init__的类其实是在一开始将类的实例所需的参数声明出来（初始化），与第二段程序中单独定义一个函数的效果是相同的
#对于只有self，不带其他参数的__init__，可以理解为显性优于隐性这层原因所以还是要加上的吧

class Have(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(self.a)
        print(self.b)

class DontHave(object):
    def donthave(self, a, b):
        self.a = a
        self.b = b
        print(self.a)
        print(self.b)

x1 = input('请输入第一个数->')
y1 = input('请输入第二个数->')
x2 = input('请输入第3个数->')
y2 = input('请输入第4个数->')

c = Have(x1, y1)

d = DontHave()
d.donthave(x2,y2)
