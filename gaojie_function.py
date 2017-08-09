#一个函数可以接受另一个函数作为参数，那么这种函数就称为高阶函数。如
def add(x,y,f):
    return f(x)+f(y)

# Python中内建了map()和reduce()函数

#可以for循环的都是Iteravle
#可以next()的都是Iterator
#可以通过iter()获得一个Iterator

#map()接受两个参数，一个是函数，一个是Iterable，将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回

r=map(list,'liudongqong')
print(list(r))
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7]))) #转换为字符串

from functools import reduce
#reduce把一个函数作用在一个序列：[x1,x2,x3...]上，这个函数必须接受两个参数，reduce把
#结果继续和序列的下一个元素做累积运算
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5,6]))

def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))


#*********************************************
#Python内建的filter()用于过滤序列。和map()类似，传入一个函数，一个序列。和map()不同的是，函数作用于每一个元素，根据返回值是True还是False
#确定保留还是删除

#筛选出偶数
def is_even_number(x):
    return x%2==0
print(list(filter(is_even_number,[1,2,3,4,5,6,7,8,9])))
#***********************************************

#筛选空字符
def not_empty(x):
    return x and x.strip()
print(list(filter(not_empty,['a','b','c',' '])))

print(sorted([10,1,5,2]))
print(sorted([10,-5,-20,1],key=abs))    #按绝对值排序