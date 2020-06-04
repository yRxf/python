def test1(*args,**dics):
    if args:
        for arg in args:
            print(arg)
    else:
        print("没有传递参数！")
    if dics:
        for key,value in dics.items():
            print(key+":"+value)
    else:
        print("没有传递字典！")

test1("dsa","das",lala="dasd",ls="das")
