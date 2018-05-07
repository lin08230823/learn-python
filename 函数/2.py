#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#L[0:3]取L列表里前3个元素 0可以省略
#L[-1] L[-2:] L[::2] 都能起作用切片返回的是list

#tuple 也可以切片不过返回的也是元组
#字符串 也可以切片返回仍是字符串


#迭代
#可以通过for循环遍历列表与元组， 这种遍历称作迭代（iteration）
#dic 和字符串也可以迭代 dic默认迭代key dic无序所以迭代结果顺序不一定相同

#我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型
from collections import Iterable
isinstance('abc', Iterable)

#列表生成器

[x*x for x in range(10)]
[m + n for m in range(3) for n in range(2)] #两层循环 

#生成器

#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
#不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
g = (x*x for x in range(10))
#g是一个生成器
next(g)#可以获得下一个返回值
for i in g:
	print(i)
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

#迭代器 ！= 可迭代对象
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#Python的for循环本质上就是通过不断调用next()函数实现的


	



