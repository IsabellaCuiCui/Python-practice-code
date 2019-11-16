#用于弄清楚super()这个函数存在的意义到底是什么
#结论：在子类中使用super后，会先执行父类同名函数的内容，再执行子类同名函数的内容。区别于前例“多重继承”中对于同名函数只执行位置靠前的类的同名函数
#运行效果：
# Parent
# Child
# Hello World! from Parent
# Child bar function
# I'm the parent.

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
#super(FooChild,self)首先找到FooChild的父类，然后把类FooChild的对象转换为类FooParent的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self,message):
        super(FooChild, self).bar(message)
        print('Child bar function')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('Hello World!')
