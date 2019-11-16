#本例用于试验多重继承在语句冲突中的效果
#运行结果为“阿里巴巴”、“百度”

class A(object):
    def general(self):
        print("阿里巴巴")

class B(object):
    def general(self):
        print("百度")

class C(A,B):
    pass

class D(B,A):
    pass

if __name__ == "__main__":
    c = C()
    c.general()
    d = D()
    d.general()
