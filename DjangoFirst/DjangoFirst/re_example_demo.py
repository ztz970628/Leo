# 正则:一种高级的字符串处理方式,通常用于字符匹配   re
# 正则是通过描述指定元素的类型和数量来进行匹配,比如手机号; 匹配 以1开头13位数字,可以实现很高精度的匹配
# 同样,编写正则的复杂程度也在提高

import re
# re.findall() 匹配所有 满足正则的条件的字符
# 匹配内容
# strings = 'hello word I am your friend_Tom'
# # 原样匹配,通常结合其他匹配使用,匹配前面是字母的o
# result = re.findall(r'o', strings)
# print(result)

# .匹配
# strings = 'hello word\n I am your friend_Tom\t'
# result = re.findall(r'.', strings)
# print(result)

# \d匹配 匹配字符串当中的数字
strings = 'hello word\n I am your friend_Tom\t 18月12 years old'
result = re.findall(r'\d{1,2}', strings)
print(result)


# \D匹配 匹配字符创当中的非数字
# strings = 'hello word\n I am your friend_Tom\t 18 years old'
# result = re.findall(r'\D', strings)
# print(result)

# \w 匹配字符创当中的 匹配数字 , 字母 , 下划线
# \W 匹配字符创当中的 匹配非数字 , 非字母 , 非下划线

#[] 匹配当中任意一个元素
# strings = 'hello word\n I am your friend_Tom\t 18 years old'
# result = re.findall(r'[ho]', strings)
# result1 = re.findall(r'[^ho]', strings)
# print(result)
# print(result1)

#() 组匹配成对的字符串  会将组外的匹配条件,做为条件匹配,返回组内匹配到的内容
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'\d\w', strings)  # 匹配一个数字和一个数字字母下划线
# result1 = re.findall(r'(\d)\w', strings)  # 匹配一个后面跟着数字字母下划线的数字
# print(result)
# print(result1)


# ()命名组 ?P<名称> 这样的格式起名字
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'(?P<hello>\d)', strings)
# print(result)


# 匹配的数量
# * 匹配任意多个 匹配0-多次为成功
# strings = 'hello word\n I am your friend_Tom\t 18 years old'
# result = re.findall(r'.*', strings)
# print(result)

# + 匹配1-多次为成功
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'.+', strings)
# print(result)

# ? 匹配0-1次
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'.?', strings)
# print(result)


# {} 匹配指定的位数
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'.{3}', strings)
# print(result)




# 特殊的匹配
# ^ 开头
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'^.{3}', strings)
# print(result)

# $ 结尾
# strings = 'hello word\n I am your friend_Tom\t 180a years old'
# result = re.findall(r'.{3}$', strings)
# print(result)