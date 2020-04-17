#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>
# -----------------------------序列化<br>
j = json.dumps(dic)
print(type(j))  # <class 'str'>
f = open('序列化对象', 'w')
f.write(j)  # -------------------等价于json.dump(dic,f)
f.close()

# -----------------------------反序列化<br>
f = open('序列化对象')
data = json.loads(f.read())  # 等价于data=json.load(f)
print(data)

# 注意点
# dct="{'1':111}"#json 不认单引号
# dct=str({"1":111})#报错,因为生成的数据还是单引号:{'one': 1}

dct = '{"1":"111"}'
print(json.loads(dct))

# conclusion:
#        无论数据是怎样创建的，只要满足json格式，就可以json.loads出来,不一定非要dumps的数据才能loads


