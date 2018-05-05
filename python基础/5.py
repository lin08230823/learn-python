#dict和set

#dict
#python内置了字典 使用键-值（key-value）存储，具有极快的查找速度
d = {'michael':95, 'bob':75}
#d[michael] = 95


'Tomas' in d , d.get('TOMAS') #判断key是否在字典里
#删除key 用.pop（）value 也会被删除

#dic 内部存放顺序是和key放入顺序无关 dic的key必须为不可变对象 dic根据key算出value的储存位置 通过哈希算法
#dic 查找速度极快，不会随着key增加变慢      需要大量的内存，浪费内存多

#list 查找和插入的时间随元素增加增加         占用空间小，内存浪费少




#set

#set也是一组key的集合 无序 要创建一个set需要输入一个列表 key 不能重复
s  = set([1,2,3,4])
# add(key)可以添加元素 但不能重复remove(key)可以删除元素



#str 不可变对象 
a = 'abc'
b = a.replace('a','A')
#b = 'Abc' a = 'abc'

# a是变量 指向的是字符串'abc' 调用replace()字符串'abc'没有发生变化 产生了一个新的字符串'Abc'并赋值给变量b


