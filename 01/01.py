#!/usr/bin/python3
'''

多行注释
缩进代表代码块
'''
# print('hello world')
# if True:
#     print('true')
# else:
#     print('false')

# 数据类型
'''
Number(数值)
int
float
bool
complx

String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

'''
# a = 10
# b = 2.3
# c = True
# e = False
# d = 3 + 4j
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print('type')
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
'''
变量命名规则同js，无需生命
'''
# 多变量复制
# a=b=c=1
# a,b,c=1,2.3,'abc'
# 删除
# del a

# 运算符
'''
算术运算符
6%5===1
2**3===8
7//3===2
'''

'''
比较运算符
==
！=
> < >= <=
赋值运算
=
+=
-=
*=
/=
%=
**=
//=

逻辑运算符
and or not
位运算符
& | ^ ~ << >>
成员运算符
in
not in

身份预算符
is 
is not
'''
'''
优先级
'''

# 字符串 ，字符串不可更改
# a = 'abc'
# b = "abc"
# c = """
# hello
# world
"""
# 拼接
# print(a + b + c)
# 更改
# 截取 [起始下标:结束下标]
# str1 = 'abcdef'
# print(str1[:2] + '123' + str1[2:])
# 格式化 %d %x %s
# print('ABCD%d' % (12345))
# print('ABCD%x' % (100))
# print('name:%s,age:%d' % ('tom', 18))
# 字符串函数
"""
# 函数
'''
def funcname (arg):
    funbody
'''

# def hello(str):
#     print('hello %s' % (str))
# 
# 
# hello('tom')
# 
# 
# def add(a, b):
#     return a + b
# 
# 
# print(add(1, 3))
# 
# 
# def f1(a=1, b=4):
#     return a + b
# 
# 
# print(f1())

# 变量作用域
'''
L local 局部
E enclosing  闭包函数外的函数中
G global 全局
B built-in 内建作用域

function04 寻找变量的时候按照从内到外的顺序查找
外边无法访问内部变量

pass占位
'''

# x = int(32)  # 内建作用域
# g_a = 0  # 全局作用域
# 
# 
# def function03():
#     o_c = 1  # 闭包函数外的函数中
# 
#     def function04():
#         i_b = 3  # 局部作用域


'''
模块 .py 文件

'''

# import sys
# 
# print(sys.path)

# import m1
# m1.m1()

# from m1 import m1
# 
# m1()
#  解释器 dir(modulename）

'''
条件控制只有if else 没有switch
嵌套注意缩进
'''

# a1 = 20
# if a1:
#     print('a1', a1)
# a2 = False
# if a2:
#     print('a2', a2)
# print('end')
#
# a3 = 10
# if a3 < 10:
#     print('<')
# elif a3 == 10:
#     print('=')
# else:
#     print('>')

'''
循环
while True:
    do smt
    
for var in list:
    do smt
    
命令行下接收键盘输入
input("tips")

int()转整型


循环可以加else
推出循环时执行一次else

range(start,end,step)
'''

# n=100
# sum=0
# counter=1
# while counter<=n:
#     sum+=counter
#     counter+=1
#
# print(sum)

# counter=1
# while counter<3:
#     counter+=1
#     print(counter)
# else:
#     print('out',counter)

# for a in [1, 2, 3, 4]:
#     print(a)
# else:
#     print('out', a)

# n = 101
# sum = 0
#
# for counter in range(1, n, 1):
#     sum += counter
# else:
#     print(sum)
#     print(counter)


'''
list
[]
tuple
元组(只读的列表)
值不可改变
(const,const,...)
sets(不可重复)
{a,b,c,...}
dictionary
{key:value,...}
'''
# list = [1, 2, 3, 1, 2, 3, 'abc', 3.14, True]
# list1 = ['aa', 'bb']
# print(list[6])
# 合并 +
# list2 = list + list1
# print(list2)

# 修改
# list[1] = 'a'
# print (list)
# list[2:5] = [2, 2, 2]
# print(list)
# 内置方法 dir(list)


