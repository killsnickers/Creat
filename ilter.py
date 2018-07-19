# -*- encoding: utf-8 -*-
# 随便定义一个list
listArray=[1,2,3]
# 使用iter()函数
iterName=iter(listArray)
print(iterName)
# 结果如下：是一个列表list的迭代器
# <list_iterator object at 0x0000017B0D984278>

print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))#没有迭代到下一个元素，直接抛出异常