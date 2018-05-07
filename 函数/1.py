#调用函数

#调用函数需要知道函数的参数和名称
#可以查看官方文档 或者在交互式命令行用help()

#函数名其实就是指向一个函数对象的引用 可以把函数名赋值给一个变量
#ex a = abs   a(-1)输出1

#定义函数
def my_abc():
	if x>=0:
		return x
	else:
		return -x
		
#如果没有return 默认return None

#pass 用作占位什么都不做
#如果有必要先对传进来的参数的数据类型做个检查
#函数可以返回多值，不过其实是一个tuple



#函数的参数

#位置参数
def power(x)
	return x*x
#对于power(x)函数 参数x就是一个位置参数 当我们调用power函数时必须传入有且只有一个参数x

def power(x, n)
	a = 1
	while n>0:
		a = a*x
		n -= 1
	return a
#对于改进后的power(x, n)函数， 有两个位置参数， 调用函数时必须按照位置依次赋值给参数



#默认参数

def power(x, n=2):
	a = 1
	while n>0:
		a = a*x
		n -= 1
	return a
#必选参数必须在前 默认参数在后 默认参数好处是降低调用函数的难度 默认参数必须指向不可变对象


#可变参数

def calc(*nums):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
	
#调用函数时可以传入任意个参数
a = [1, 2, 3]
#使用*a 可将列表当做可变参数传入



#关键字参数
#关键键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
	print('name', name, 'age', age, 'others':kw)
	
person('mic', 15)
person('mic', 15, city = 'beijing')

exit = {'city': 'beijing','job': 'engineer'}
#可以通过**exit把字典传入关键字参数

#递归函数

def fact(n):
	if n==1:
		return n
	else:
		return n*f(n-1)
		
#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
#===> 5 * (4 * (3 * (2 * 1)))
#===> 5 * (4 * (3 * 2))
#===> 5 * (4 * 6)
#===> 5 * 24
#===> 120

#使用递归需要防止栈（stack）溢出 栈后进先出
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#汉诺塔

		