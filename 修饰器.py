#通过如下代码实现输出
#<b><i>Hello</i></b>
"""
@makebold  
@makeitalic  
def say():  
   return "Hello"
"""
########################
"""
def makebold(fn):  
    def wrapped():  
        return "<b>" + fn() + "</b>"  
    return wrapped  
   
def makeitalic(fn):  
    def wrapped():  
        return "<i>" + fn() + "</i>"  
    return wrapped  
  
@makebold  
@makeitalic  
def say():  
    return "Hello" 
   
print(say())        #<b><i>Hello</i></b>
"""
"""
@makebold  
@makeitalic  
def say():  
    return "Hello"

#say()先是被makeitalic修饰然后被makebold修饰,即：
#say = makeitalic(say)      #返回makeitalic.wrapped
#say = makebold(say)        #返回makebold.wrapped
"""
"""
#如果,对装饰器进行调用,如 @w1() 后面带个括号：会直接执行里面的函数

def w1():
    print("---正在装饰1----")
    def inner(func):
        print("---1111111111----")
        func()
    return inner

@w1()
def f1():
    print("---f1---")
f1()
#>>>---正在装饰1----
#   ---1111111111----
#---f1---
#这说明,如果 @w1() 这样用 ,那么它首先会 把 w1() 函数执行一遍 , 这个时候返回的是 inner 函数的引用,那么,@w1() 就变成了 @inner 这个时候 再把f1传到了inner函数里面开始进行装饰 所以 inner 函数被执行,
"""
"""
#装饰器中带有参数:
def a1(nihao):
    def w1(func):
        print("---正在装饰1----")
        def inner():
            print("---1111111111----%s" % nihao)
            func()
        return inner
    return w1

@a1('hello~')
def f1():
    print("---f1---")

#>>>---正在装饰1----
'''过程 1. 首先执行 a1('hello~')   a1里面用 nihao 这个变量保存传递的参数,返回的是 w1 的引用
    2. 装饰器那一行 变成了 @w1 ,然后把 f1 传递进去,调用 w1 开始进行装饰
　　3. 装饰完成后 返回的 是 inner 的引用 所以 现在 f1 = inner'''
"""