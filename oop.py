class student:

	def __init__(self, name, score):
		self.__name = name  #双下划线为私有变量无法通过 实例.__name 访问 需要改名字在内部修改
		self.__score = score

	def set_name(self, name):#
		if isinstance(name, str):
			self.__name = name
		else:
			raise ValueError("error type")

	def get_name(self):
		return self.__name

a = student("刘志伟", 95)
a.set_name("徐洁安")
print(a.get_name())
