# 列表
# 列表是可变的 mtable
a = list('Hello')
print(a)

# list适用于所有类型序列

# 删除列表元素
del a[0]

print(a)

# slice 分片
print(a[2:])
## 分片赋值
a[2:]="asdas"
print(a)

## 分片赋值可以在不需要替换任何原有元素的情况下插入新的元素
numbers = [1,5]

numbers[1:1] = [2,3,4]
print(numbers)

# 分片删除
numbers[1:4]=[]

print(numbers)

# list 方法
# 新增 append 在原有的列表最后添加元素

numbers.append(6)
print(numbers)

# count 统计某个元素在列表中出现的次数
s = ['to','be','or','not','to','be']

print(s.count('to'))

# extend 在列表的末尾一次性追加另一个序列中的多个值

ex = ['is','a','question']
s.extend(ex)
s.extend('as') # extend的元素都会当成一个列表
print(s)
# extend s被替换   s+ex 返回一个新的列表
# a = a + b  效率低于 a.extend(b)

# in-place operation 原位置操作
a = [1,2,3]
b = [4,5,6]
a[len(a):]=b # 可读性差
print(a)

# index 从列表中找出某个值第一个匹配项的索引位置
print(a.index(4))

# insert 将对象插入列表中

# pop 移除列表中的一个元素，默认最后一个， 并且返回该元素的值

# pop 和 append 形成 stack    push  pop LIFO last in first out 后进先出

# pop 和 insert(0,...) 形成 queue FIFo first in first out 先进先出
# 更好的方案是 collection模块中的deque

# remove 用于移除列表中某一个值的第一个匹配项 pop 移除位置的元素返回值，remove移除值匹配的元素不返回

# reverse 反向
x = [1,2,3]
x = [4,6,2,1,7,9]
x.reverse() # 反向存放，不排序
print(x)
# sort  对原位置的列表进行排序 sorted() 函数 获取已排序的副本的方法
x.sort()
x.sort(reverse=True) # http://wiki.python.org/moin/HowTo/Sorting
print(x)
