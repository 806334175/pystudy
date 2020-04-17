#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

print(re.findall("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>"))  # ['h1']
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>").group())  # <h1>hello</h1>
print(re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>", "<h1>hello</h1>").groupdict())  # <h1>hello</h1>

print(re.search(r"<(\w+)>\w+</(\w+)>", "<h1>hello</h1>").group())
print(re.search(r"<(\w+)>\w+</\1>", "<h1>hello</h1>").group())

# 补充一


# 补充二
# import re

# 使用|，先匹配的先生效，|左边是匹配小数，而findall最终结果是查看分组，所有即使匹配成功小数也不会存入结果
# 而不是小数时，就去匹配(-?\d+)，匹配到的自然就是，非小数的数，在此处即整数
#
print(re.findall(r"-?\d+\.\d*|(-?\d+)", "1-2*(60+(-40.35/5)-(-4*3))"))  # 找出所有整数['1', '-2', '60', '', '5', '-4', '3']

# 找到所有数字:
print(re.findall('\D?(\-?\d+\.?\d*)', "1-2*(60+(-40.35/5)-(-4*3))"))  # ['1','2','60','-40.35','5','-4','3']

# 计算器作业参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html
expression = '1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

content = re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)', expression).group()  # (-3-40.0/5)
