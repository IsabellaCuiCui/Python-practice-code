# 用于测试random模块中各类函数的效果
#本例涉及的函数:random.random() / uniform() / randint() / choice() / shuffle()

import random

a = random.random() #用于生成一个随机的0~1之间的浮点数
b = random.uniform(1, 5) # 用于生成一个有范围的浮点数
c = random.randint(-11, -5) #用于生成一个有范围的整数

d1 = [1 ,2.2, 3.3, 4.4, 5, 6]
d = random.choice(d1) #用于从列表中选取元素返回

e1 = "abcdefg"
e = random.choice(e1) #用于从字符串中选取元素返回

print(a)
print(b)
print(c)
print(d)
print(e)

random.shuffle(d1)
print(d1) #注意print的不是rando.shuffle(d1),而是先调用函数后，再print变量d1，否则会返回None值
#random.shuffle函数不支持对字符串的乱序，random.shuffle(e1)会报错

f = list(range(10)) #f=range(10)
print(f)
random.shuffle(f)
print(f)

slice = random.sample(f, 5)
print(slice)
