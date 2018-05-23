# -*- coding:utf-8 -*-
#二分查找
def binary_search(list, item):
	low = 0
	high = len(list)-1
	while low<=high:
		mid = (low + high)//2
		guess = list[mid]
		if guess>item:
			high = mid-1
		elif guess<item:
			low - mid+1
		else:
			return mid
	return None

#快排
def quick_sort(list):
	if len(list)<2:
		return list
	mid = list[0]
	smalllist = [i for i in list[1:] if i<=mid]
	biglist = [i for i in list[1:] if i>mid]
	finallylist = quick_sort(smalllist) + [mid] + quick_sort(biglist)

