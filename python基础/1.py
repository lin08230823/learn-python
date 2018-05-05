#数据类型和变量


#python中能够直接处理的数据类型

#整数
#十进制1,100,-8080 十六进制0xff00,0xab517c

#浮点数 
#1.23,2.41,-9.01 科学计数法1.23e9,1.25e-5 整数运算精确 浮点不一定

#字符串 
#'abc',"xyz"  "I'm ok" 'I\'m \"ok\"'  \转义字符 
print('I\'m ok')
#I'm ok
print('i\'m learning\npython')
#I'm learning
#python

#布尔值
#True or False 

#空值
#None 不能理解为0

#变量 
#变量名必须是大小写英文，数字，_的组合，且不能用数字开头
a = 1
t_007 = 'T007'
answer = True
#python中=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123
print(a)
a = 'ABC'
print(a)
#变量本身不固定为动态语言 静态语言定义变量时需指定变量类型

a = 'abc'
#解释器做了两件事
#1、内存中创建'abc'字符串 2、创建变量a并将a指向'abc'

a = 'ABC'
b = a
a = 'XYZ'
# b = 'ABC' a = 'XYZ'