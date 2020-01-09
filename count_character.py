"""
这个程序用于统计文本中每个字符出现的次数
使用了字典中的setdefault函数
source：《python编程快速上手-让繁琐工作自动化》
"""
import pprint #用于漂亮的输出打印

#初始化变量
sentence = "It was a bright cold day in April."

#统计字符出现次数（可以再进一步封装成函数）
for character in sentence:
	count.setdefault(character,0)  #注意setdefault()的用法
	count[character] = count[character] + 1
  
pprint.pprint(count)
