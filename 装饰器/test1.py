#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 下午12:40
# @Author  : Ryu
# @Site    : 
# @File    : test1.py
# @Software: PyCharm


def zhuangshi(func):
    def inner(*args, **kwargs):
        print("开始")
        res = func(*args, **kwargs)
        print("结束")
        return res

    return inner


def mytest(a,b):
    def x(func):
        def y(*args, **kwargs):
            print(a)
            res = func(*args, **kwargs)
            print(b)
            return res
        return y
    return x


@mytest(1,2)
def a():
    print("凯撒")


@mytest(1,2)
def b(x):
    print(x)


@mytest(1,2)
def c(x, y):
    print(x + y)


a()
b("第二个")
c("我海外", "你")


# ---------------装饰器带参数-------------------
# 认证函数
def auth(request, kargs):
    print("认证成功！")


# 日志函数
def log(request, kargs):
    print("日志添加成功")


# 装饰器函数。接收两个参数，这两个参数应该是某个函数的名字。
def Filter(auth_func, log_func):
    # 第一层封装，f1函数实际上被传递给了main_fuc这个参数
    def outer(main_func):
        # 第二层封装，auth和log函数的参数值被传递到了这里
        def wrapper(request, kargs):
            # 下面代码的判断逻辑不重要，重要的是参数的引用和返回值
            before_result = auth(request, kargs)
            if (before_result != None):
                return before_result;

            main_result = main_func(request, kargs)
            if (main_result != None):
                return main_result;

            after_result = log(request, kargs)
            if (after_result != None):
                return after_result;

        return wrapper

    return outer


# 注意了，这里的装饰器函数有参数哦，它的意思是先执行filter函数
# 然后将filter函数的返回值作为装饰器函数的名字返回到这里，所以，
# 其实这里，Filter(auth,log) = outer , @Filter(auth,log) =  @outer
@Filter(auth, log)
def f1(name, age):
    print("%s 正在连接业务部门1数据接口......" % name)

# 调用方法
# f1("jack", 18)
