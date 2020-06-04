import sys
first_number = input("请输入被除数：")
second_number = input("请输入除数：")
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("输入的内容非数字！")
    sys.exit(1)
try:
    answer = first_number / second_number
except ZeroDivisionError:
    print("除数不能为0")
else:
    print(answer)