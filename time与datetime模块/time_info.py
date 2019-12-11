#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# --------------------------我们先以当前时间为准,让大家快速认识三种形式的时间
print(time.time())  # 时间戳:1487130156.419527
print(time.strftime("%Y-%m-%d %X"))  # 格式化的时间字符串:'2017-02-15 11:40:53'

print(time.localtime())  # 本地时区的struct_time
print(time.gmtime())  # UTC时区的struct_time

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

#
# 格式化字符串的时间格式
# %a    Locale’s abbreviated weekday name.
print("周几的缩写")
print(time.strftime("%a"))
# %A    Locale’s full weekday name.
print("周几的全称")
print(time.strftime("%A"))
# %b    Locale’s abbreviated month name.
print("月份的缩写")
print(time.strftime("%b"))
# %B    Locale’s full month name.
print("月份的全称")
print(time.strftime("%B"))
# %c    Locale’s appropriate date and time representation.
print("当地适当的日期和时间表示")
print(time.strftime("%c"))
# %d    Day of the month as a decimal number [01,31].
print("当前月份的第几天")
print(time.strftime("%d"))
# %H    Hour (24-hour clock) as a decimal number [00,23].
print("当天24小时的第几个小时")
print(time.strftime("%H"))
# %I    Hour (12-hour clock) as a decimal number [01,12].
print("当天24小时的第几个小时")
print(time.strftime("%I"))
# %j    Day of the year as a decimal number [001,366].
print("一年中的第几天")
print(time.strftime("%j"))
# %m    Month as a decimal number [01,12].
print("第几个月")
print(time.strftime("%m"))
# %M    Minute as a decimal number [00,59].
print("第几分钟")
print(time.strftime("%M"))
# %p    Locale’s equivalent of either AM or PM.    (1)
print("AM表示上午，PM表示下午")
print(time.strftime("%p"))
# %S    Second as a decimal number [00,61].    (2)
print("第几秒")
print(time.strftime("%S"))
# %U    Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
print("一年中的第几周（星期日为一周的第一天），十进制数字[00,53]。新年中第一个星期日之前的所有天都被视为第0周。")
print(time.strftime("%U"))
# %w    Weekday as a decimal number [0(Sunday),6].
print("这周的第几天，星期天为0")
print(time.strftime("%w"))
# %W    Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
print("一年中的第几周（星期日为一周的第一天），十进制数字[00,53]。新年中第一个星期日之前的所有天都被视为第0周。")
print(time.strftime("%W"))
# %x    Locale’s appropriate date representation.
print("本地的适当日期表示")
print(time.strftime("%x"))
# %X    Locale’s appropriate time representation.
print("本地的适当时间表示")
print(time.strftime("%X"))
# %y    Year without century as a decimal number [00,99].
print("以十进制数表示的无世纪的年份")
print(time.strftime("%y"))
# %Y    Year with century as a decimal number.
print("以世纪为十进制数的年份")
print(time.strftime("%Y"))
# %z    Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
print("时区偏移量，表示与UTC/GMT的正时差或负时差，格式为+h m m或-h m m，其中h表示十进制小时数字，m表示十进制分钟数字[-23:59，+23:59]")
print(time.strftime("%z"))
# %Z    Time zone name (no characters if no time zone exists).
print("当前时区的名称")
print(time.strftime("%Z"))
# %%    A literal '%' character.
print("%符号本身")
print(time.strftime("%%"))

# ----------------------------


# --------------------------按图1转换时间
# localtime([secs])
# 将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
time.localtime()
time.localtime(1473525444.037215)

# gmtime([secs]) 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

# mktime(t) : 将一个struct_time转化为时间戳。
print(time.mktime(time.localtime()))  # 1473525749.0

# strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个
# 元素越界，ValueError的错误将会被抛出。
print(time.strftime("%Y-%m-%d %X", time.localtime()))  # 2016-09-11 00:49:56

# time.strptime(string[, format])
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))
# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6,
#  tm_wday=3, tm_yday=125, tm_isdst=-1)
# 在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。


# --------------------------按图2转换时间
# asctime([t]) : 把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'。
# 如果没有参数，将会将time.localtime()作为参数传入。
print(time.asctime())  # Sun Sep 11 00:43:43 2016

# ctime([secs]) : 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为
# None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。
print(time.ctime())  # Sun Sep 11 00:46:38 2016
print(time.ctime(time.time()))  # Sun Sep 11 00:46:38 2016
