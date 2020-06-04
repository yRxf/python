import sys
#读写文件
"""
open(filename,'w')
第一个参数，文件位置，文件名
第二个参数，打开方式，默认以只读('r')方式打开
只读('r')、只写('w')、附加('a')、读写('r+')
只写('w')方式会清空原文件内容、附加('a')、('r+')方式会将内容写到文件末尾
"""
filename = "test.txt"
"""
try:
    with open(filename) as file_:
        print(file_.read())
except FileNotFoundError:
    print("文件不存在！")
    sys.exit(1)
"""
"""
with open(filename,'w') as file_:
    file_.write("3.1415926535")
with open(filename,'r') as file_:
    print(file_.read())
with open(filename,'a') as file_:
    file_.write("\n  8979323846")
    file_.write("\n  2643383279")
"""
"""
#逐行读取
with open(filename,'r') as file_:
    for line in file_:
        print(line.rstrip())        #有关指针？已指向末尾，所以下面为空列表
    lines = file_.readlines()       #逐行读取存入列表
    print(lines)    
"""
"""
3.1415926535
3.1415926535
  8979323846
  2643383279
[]
"""
"""
with open(filename,'w') as file_:
    file_.write("3.1415926535")
    file_.write("\n  8979323846")
    file_.write("\n  2643383279")
    file_.write("\n  5028841971")
    file_.write("\n  6939937510")
with open(filename) as file_:
    lines = file_.readlines()
content = ""
for line in lines:
    content += line.strip()
print(content)      #3.14159265358979323846264338327950288419716939937510
"""

#json格式存储数据
#json.dump()  存储   json.load()  读取
"""需要注意json存储的格式"""
import json
numbers = list(range(0,6))
filename2 = "numbers.json"
with open(filename2,'w') as f_j:
    json.dump(numbers,f_j)          #[0, 1, 2, 3, 4, 5]

with open(filename2) as f_j:
    r_numbers = json.load(f_j)
print(r_numbers)

