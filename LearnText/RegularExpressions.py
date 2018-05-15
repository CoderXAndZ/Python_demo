#! /usr/local/bin/python3
# -*- coding: UTF-8 -*-
# 正则表达式

import re

'''
简单正则表达式
'''
result = re.search(r'Love','I Love you')
print(result) # <_sre.SRE_Match object; span=(2, 6), match='Love'>

result1 = re.search(r'\.','www.com') # 匹配.
print(result1) # <_sre.SRE_Match object; span=(3, 4), match='.'>

# 匹配一个数字
result2 = re.search(r'\d','www.123.com')
print(result2) # <_sre.SRE_Match object; span=(4, 5), match='1'>

# 匹配三个数字
result3 = re.search(r'\d\d\d','www.123.com')
print(result3) # <_sre.SRE_Match object; span=(4, 7), match='123'>

# 字符类：只要匹配这个字符类中的任何一个字符，都算匹配
# 1>匹配元音字母
result4 = re.search(r'[aeiou]','I love you')
print(result4) # <_sre.SRE_Match object; span=(3, 4), match='o'>
# 2>匹配字母
result5 = re.search(r'[a-z]','I love you')
print(result5) # <_sre.SRE_Match object; span=(2, 3), match='l'>
# 3>匹配数字
result6 = re.search(r'[0-9]','I love you 123')
print(result6) # <_sre.SRE_Match object; span=(11, 12), match='1'>
result7 = re.search(r'[2-9]','I love you 123')
print(result7) # <_sre.SRE_Match object; span=(12, 13), match='2'>

# 文字重复的确定次数
result8 = re.search(r'co{2}c','I love cooca')
print(result8) # <_sre.SRE_Match object; span=(7, 11), match='cooc'>
# 文字重复的次数范围
result9 = re.search(r'co{1,3}c','I love cooca')
print('9次：',result9) # <_sre.SRE_Match object; span=(7, 11), match='cooc'>

# 正则表达式匹配的是字符串，数字对于字符来说，只有0-9，例如，123是由1，2，3 三个字符组成的
#匹配  0-255
result10 = re.search(r'[01]\d\d|[2[0-4]\d|25[0-5]','数字是：128')
print('10次：',result10) #  <_sre.SRE_Match object; span=(4, 7), match='128'>
result11 = re.search(r'[01]\d\d|[2[0-4]\d|25[0-5]','数字是：257')
print('11次：',result11) # <_sre.SRE_Match object; span=(4, 6), match='25'>
# 匹配 ip 地址
result12 = re.search(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}','ip地址是：192.168.1.1')
print('12次：',result12) # <_sre.SRE_Match object; span=(6, 18), match='128.103.2.30'>

'''
正则表达式语法
'''
# . 表示匹配除换行符之外的任意字符 1.通过re.DOTALL标识可以使.匹配任何字符（包含换行符）
# | 或 下面匹配m或n
res = re.search(r'Co(m|n)','www.Com')
print(res) # <_sre.SRE_Match object; span=(4, 7), match='Com'>
res1 = re.search(r'Co(m|n)','www.Con')
print(res1) # <_sre.SRE_Match object; span=(4, 7), match='Con'>
res2 = re.search(r'Co(m|n)','www.CoD')
print(res2) # None

# ^ 脱字符，匹配输入字符串的开始位置   下面的C必须是字符串的开头
res3 = re.search(r'^CoD','www.CoD')
print(res3) # None
res4 = re.search(r'^CoD','CoD.www')
print(res4) #<_sre.SRE_Match object; span=(0, 3), match='CoD'>

# $ 匹配输入字符串的结束位置   下面的C必须是字符串的开头
res5 = re.search(r'D$','CoD.www')
print(res5) # None
res6 = re.search(r'CoD$','www.CoD')
print(res6) # <_sre.SRE_Match object; span=(4, 7), match='CoD'>

# \ 1.将一个普通字符变成特殊字符，例如，\d表示匹配所有十进制数字；2.解除元字符的特殊功能，例如，\.表示匹配点号本身；
#   3.如果数字是1-99，那么含义是引用序号对应的子组（小括号括起来的值，把一个东西当成一个整体）所匹配的字符串；如果数字是0或者3位数字，那么它是一个八进制数，表示的是这个八进制数对应的Asics码的字符
res6 = re.search(r'(com)\1','www.com') # (com)\1 等价于 comcom
print(res6) # None
res7 = re.search(r'(com)\1','comcom.www') # (com)\1 等价于 comcom
print(res7) # <_sre.SRE_Match object; span=(0, 6), match='comcom'>
# 16进制的 30 对应的Asics码就是 0，八进制是60，
res8 = re.search(r'(com)\060','com0.www') # 3位数就是060
print(res8) # <_sre.SRE_Match object; span=(0, 4), match='com0'>
# 10进制的 97 对应的Asics码就是 a，八进制是141
res9 = re.search(r'(com)\141','coma.www')
print(res9) # <_sre.SRE_Match object; span=(0, 4), match='coma'>

# [...] 生成字符类，匹配所包含的任意一个字符
# 1.连字符 - 如果出现在字符串中间表示字符范围描述；如果出现在首位则仅作为普通字符；
# 2.特殊字符仅有反斜线 \ 保持特殊含义，用于转译字符，其他的特殊字符如 *、+、？等均作为普通字符匹配；
# 3.脱字符 ^ 如果出现在首位则表示匹配不包含其中的任意字符；如果 ^ 出现在字符串中间就仅作为普通字符匹配
# 匹配 .
res10 = re.search(r'[.]','coma.www')
print(res10) # <_sre.SRE_Match object; span=(4, 5), match='.'>
# 匹配 a-z，并以数组返回
res11 = re.findall(r'[a-z]',"com.www")
print(res11) # ['c', 'o', 'm', 'w', 'w', 'w']
# 匹配特殊字符反斜线
res12 = re.findall(r'[\n]',"com.www")
print(res12) # ['\n']
# 匹配不包括 a-z的字符
res13 = re.findall(r'[^a-z]',"CoM.www")
print(res13) # ['C', 'M', '.']

# {M,N} M 和 N 均为非负整数，其中 M <= N,表示前边的 RE 匹配 M ~ N 次
# 1.{M,} 表示至少匹配 M 次
# 2.{,N} 等价于{0,N}
# 3.{N} 表示需要匹配 N 次

resu = re.search(r'w{3}','www.com')
print(resu) # <_sre.SRE_Match object; span=(0, 3), match='www'>
resu1 = re.search(r'(com){1,3}','comcomcom')
print(resu1) # <_sre.SRE_Match object; span=(0, 9), match='comcomcom'>

# * 匹配前面的子表达式零次或多次，等价于{0,}

# + 匹配前面的子表达式一次或多次，等价于{1,}

# ? 匹配前面的子表达式零次或一次，等价于{0,1}

# 正则表达式的贪婪
# 关于重复操作，正则表达式默认启用的贪婪模式来进行匹配的，只要在符合的条件下会尽可能多的去匹配
s = '<html><title>I love progamming</title></html>'
str = re.search(r'<.+>',s)
print(str) # <_sre.SRE_Match object; span=(0, 45), match='<html><title>I love progamming</title></html>'>

# 启用非贪婪模式：在表示重复的元字符后面加上一个 ? 号就可以了，这时候 ? 表示启用非贪婪模式，而不是表示0次或1次
s1 = '<html><title>I love progamming</title></html>'
str1 = re.search(r'<.+?>',s1)
print(str1) # <_sre.SRE_Match object; span=(0, 6), match='<html>'>
