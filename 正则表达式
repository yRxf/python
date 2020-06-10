#re.match函数:re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#re.search方法:re.search 扫描整个字符串并返回第一个成功的匹配。
#re.compile 函数:compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
#re.findall:在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#re.finditer:和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.split:split 方法按照能够匹配的子串将字符串分割后返回列表
"""正则表达式模式"""
#在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字
#.可以匹配任意字符
#用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
#可以用[]表示范围
#A|B可以匹配A或B
#^表示行的开头，^\d表示必须以数字开头
#^表示行的开头，^\d表示必须以数字开头

"""
re*:匹配0个或多个的表达式。
re+:匹配1个或多个的表达式。
re?：匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}：精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}：匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
re{ n, m}：匹配 n 到 m 次由前面的正则表达式定义的片段
a| b：匹配a或b
(?imx)：正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)：正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)：类似 (...), 但是不表示一个组
(?#...)：注释.
(?= re)：前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)：前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)：匹配的独立模式，省去回溯。

\w：匹配字母数字及下划线
\W：匹配非字母数字及下划线
\s：匹配任意空白字符，等价于 [\t\n\r\f].
\S：匹配任意非空字符
\d：匹配任意数字，等价于 [0-9].
\D：匹配任意非数字
\A：匹配字符串开始
\Z：匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z:匹配字符串结束
\G:匹配最后匹配完成的位置。
\b:匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B:匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.:匹配一个换行符。匹配一个制表符。等
\1...\9:匹配第n个分组的内容。
\10:匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


[Pp]ython:匹配 "Python" 或 "python"
[aeiou]:匹配中括号内的任意一个字母
[0-9]:匹配任何数字。类似于 [0123456789]
[a-zA-Z0-9]:匹配任何字母及数字
[^0-9]:匹配除了数字外的字符
"""


"""关于修饰符"""
#re.I：使匹配对大小写不敏感
#re.L：做本地化识别（locale-aware）匹配
#re.M：多行匹配，影响 ^ 和 $
#re.S：使 . 匹配包括换行在内的所有字符
#re.U：根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
#re.X：该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

#re.match从开始位置进行匹配，如果匹配成功，则返回一个re.Match object;对象，失败返回None
#re.match(pattern, string, flags=0)
#pattern:匹配的正则表达式
#string:要匹配的字符串。
#flags:标志位，用于控制正则表达式的匹配方式
#
# import re
#f = lambda rr,flag=True: print(rr.groups() if hasattr(rr, 'groups') and flag else rr)
#rr = re.match('www', 'www.baidu.com')   #<re.Match object; span=(0, 3), match='www'>
#print(rr.span())                        #(0, 3)
#print(re.match('com', 'www.baidu.com')) #None
#group(num=0):匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
#groups():返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
#组是通过 "(" 和 ")" 元字符来标识的。
#可以使用?P<name>   给组命名A
#.groupdict()       以字典形式输出
#line = "Cats Are smarter than dogs"
#rr = re.match( r'(?P<first>.*) are (.*?) .*', line)      #(.*)为一个组，(.*?)为一个组                      #None
#rr = re.match( r'(?P<first>.*) are (.*?) .*', line,re.I)      #re.I大小写不敏感，故匹配成功
"""
if rr is not None:
    print(rr.group())          #.group()为整个结构： Cats are smarter than dogs
    print(rr.group(1))          #Cats
    print(rr.group('first'))          #Cats
    print(rr.group(2))          #smarter
    print(rr.group(1,2))          #('Cats', 'smarter')
    print(rr.groups())          #('Cats', 'smarter')
"""
#re.search：扫描整个字符串并返回第一个成功的匹配。
#re.match与re.search的区别：
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
#re.search匹配整个字符串，直到找到一个匹配。可以是在字符串的任意位置
#rr = re.search('com', 'www.baidu.com')     #<re.Match object; span=(11, 14), match='com'>

#检索和替换
#re.sub(pattern, repl, string, count=0, flags=0)
#pattern : 正则中的模式字符串。
#repl : 替换的字符串，也可为一个函数。
#string : 要被查找替换的原始字符串。
#count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
#phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
#num = re.sub(r'#.*$', "", phone)        #匹配#到最后所有的字符，替换为""
#f(num)                           #2004-959-559
#num = re.sub(r'\D', "", phone)        #匹配所有非数字字符   2004959559
"""将字符串里的数字*2"""
#s = 'A135c79b246d80'
#s = re.sub(r'(\d+)', lambda value: str(int(value.group(1))*2), s)       #A270c158b492d160

#re.compile 函数:用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
#re.compile(pattern[, flags])
#pattern : 一个字符串形式的正则表达式

#pattern = re.compile(r'\d+')        #用于匹配至少一个数字
#m = pattern.match(s)    #None
#m = pattern.match(s,1,2)    #从第二个位置到第三个（不包含第三个）开始匹配，下标从0开始，<re.Match object; span=(1, 2), match='1'>
#f(m)                        #()   即存在groups属性
#print(m.group())            #135
#print(m.start())            #1
#print(m.end())            #2
#print(m.span())            #(1, 2)

#findall：在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#注意： match 和 search 是匹配一次 findall 匹配所有。
#findall(string[, pos[, endpos]])
#string : 待匹配的字符串。
#pos : 可选参数，指定字符串的起始位置，默认为 0。
#endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
#rr = pattern.findall(s)       #['135', '79', '246', '80']
#rr = pattern.findall(s, 0, 10) #['135', '79', '24']

#re.finditer:和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
#re.finditer(pattern, string, flags=0)
#it = re.finditer(r'\d+',"12a32bc43jf3") 
#it = pattern.finditer("12a32bc43jf3") 
#for match in it: 
#    print (match.group())

#re.split：按照能够匹配的子串将字符串分割后返回列表
#re.split(pattern, string[, maxsplit=0, flags=0])
#maxsplit 最大分割次数
#rr = pattern.split(s,1)         #['A', 'c79b246d80']    以数字进行分割
#rr = pattern.split(s)         #['A', 'c', 'b', 'd', '']
#f(rr)
