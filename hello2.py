"""
list_ = 'hello world!'.split()
print(list_)
"""
#import collections
#Card = collections.namedtuple('Card',['rank','suit'])
#Card = collections.namedtuple(name,[arg1,arg2,...])
#print(Card('7','diamonds'))    #Card(rank='7', suit='diamonds')
'''
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self.cards_ = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
        """
        [Card(rank='2', suit='spades'),
         Card(rank='3', suit='spades'),
         ...]
        生成52来张牌
        """
    """定义len()方法"""
    def __len__(self):      #提供len()方法
        return len(self.cards_)
    #输出格式print(len(FrenchDeck()))
    """
    def len(self):
        return len(self.cards_)
    #输出格式print(FrenchDeck().len())
    """
    def __getitem__(self,position):     #提供下标选择方法
        return self.cards_[position]
'''

#deck = FrenchDeck()

#__len__
#print(len(deck))
#__getitem__
#print(deck[0])      #Card(rank='2', suit='spades')

#from random import choice       #在一个序列中随机选择元素
#print(choice(deck))             #Card(rank='10', suit='hearts')
#print(choice(deck))             #Card(rank='9', suit='clubs')

#print(deck[12::13])             #12开始每过13取一次     所有的A
#for card in reversed(deck):     #反向迭代
#    print(card)
#print(list(reversed(deck))[0])  #Card(rank='A', suit='hearts')
#print(deck.suit_values)

#suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
"""
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
"""
#print(deck[17].rank)
#查找deck[17].rank在FrenchDeck.ranks中第一个出现的位置
#print(FrenchDeck.ranks.index(deck[17].rank))     #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#index(arg)        查找第一个arg出现的位置
#按spades_high(deck)进行排序
#for card in sorted(deck,key=spades_high):
#    print(card)

'''
"""一个简单的二维向量类"""
from math import hypot

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #重写输出  print
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    #模运算
    def __abs__(self):
        return hypot(self.x, self.y)
    #是否为0向量
    def __bool__(self):
        #return bool(abs(slef))
        return bool(self.x or self.y)
    #向量加法  +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    #数乘   *
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)

    def __rmul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)

#print(bool(Vector()))
#print(Vector(1,1)+Vector(2,6))      #Vector(3, 7)
#print(Vector(2,5)*2)                #Vector(4, 10)
#print(2*Vector(2,5))                #Vector(4, 10)  调用__rmul__
'''
"""ord()函数，返回ASCII码"""

#判断对象是否包含蘑菇属性
#hasattr(object, name)：判断对象object是否包含名为name的特性
#使用dir方法：dir(object) 返回所有属性