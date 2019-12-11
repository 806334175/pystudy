#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1、什么叫hash:hash是一种算法（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法），该算法接受传入的内容，经过运算得到一串hash值
# 2、hash值的特点是：
#     2.1 只要传入的内容一样，得到的hash值必然一样=====>要用明文传输密码文件完整性校验
#     2.2 不能由hash值返解成内容=======》把密码做成hash值，不应该在网络传输明文密码
#     2.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的

# hash.digest()
# 返回摘要，作为二进制数据字符串值
#
# hash.hexdigest()
# 返回摘要，作为十六进制数据字符串值


import hashlib

# ######## md5 ########

m = hashlib.md5()  # m=hashlib.sha256()

m.update('hello'.encode('utf8'))
print(type(m.hexdigest()))  # 5d41402abc4b2a76b9719d911017c592
print(m.hexdigest())  # 5d41402abc4b2a76b9719d911017c592

m.update('alvin'.encode('utf8'))

print(m.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af

m2 = hashlib.md5()
m2.update('helloalvin'.encode('utf8'))
print(m2.hexdigest())  # 92a7e713c30abbb0319fa07da2a5c4af

'''
注意：把一段很长的数据update多次，与一次update这段长数据，得到的结果一样
但是update多次为校验大文件提供了可能。
'''

# 以上加密算法虽然依然非常厉害，但时候存在缺陷，即：通过撞库可以反解。所以，有必要对加密算法中添加自定义key再来做加密。


# ######## sha256 ########

hash = hashlib.sha256('898oaFs09f'.encode('utf8'))
hash.update('alvin'.encode('utf8'))
print(hash.hexdigest())  # e79e68f070cdedcfe63eaf1a2e92c83b4cfb1b5c6bc452d214c1b7e77cdfd1c7

########## 模拟撞库破解密码#################


##自己库中的密码
passwds = [
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
]


def make_passwd_dic(passwds):
    dic = {}
    for passwd in passwds:
        m = hashlib.md5()
        m.update(passwd.encode('utf-8'))
        dic[passwd] = m.hexdigest()
    return dic


def break_code(cryptograph, passwd_dic):
    for k, v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>\033[46m%s\033[0m' % k)


cryptograph = 'aee949757a2e698417463d47acac93df'
break_code(cryptograph, make_passwd_dic(passwds))







