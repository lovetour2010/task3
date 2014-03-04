# -*- coding: utf-8 -*-
from sys import exit
def start(sum):
    print '''
	Welcome!
	开始你有3分，在游戏过程中，如果分数为0，马上退出游戏。
	让我们开始吧！
	现在你走在去外婆的乡间小路上。
	Oh，前面有个红蘑菇！是否要采摘（注意：可能会有毒哦）？请输入\'yes\' 或者 \'no\': '''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum-1
		    print "真倒霉，红蘑菇有毒，你已经被扣1分了" 
		    score(sum)
		    boat(sum)
	    elif next=="no":
		    print "继续往前走吧……"
		    boat(sum)
	    else:
		    print "不明白你的意思!"
	   
def boat(sum):
    print '''
    Oh，前面有条河，如果坐船到对岸会近些，不过需要花费1分，也可以选择继续走路。
    是否要坐船？请输入\'yes\' 或者 \'no\': '''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum-1
		    print "坐船扣1分" 
		    score(sum)
		    fish(sum)
	    elif next=="no":
		    print "继续往前走吧……"
		    road(sum)
	    else:
		    print "不明白你的意思!"
	
def fish(sum):
    print '''坐上船感觉不错吧！河里有很多鱼，你只能捞一种。
    你要捞红色的还是蓝色的鱼？请输入\'red\' 或者 \'blue\':'''
	
    while True:
	    next=raw_input(">")
	    if next=="red":
		    sum=sum-1
		    print "非常遗憾，此鱼有毒，你被扣了1分" 
		    score(sum)
		    win()
	    elif next=="blue":
		    print "运气不错加1分，现在还剩%s分" %sum
		    win()
	    else:
		    print "不明白你的意思!"
	
def road(sum):
    print '''有个老婆婆向你走过来，原来她是想问路（注意:可能是骗子哦）。
    是否要指路？请输入\'yes\' 或者 \'no\':'''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum+1
		    print "心肠不错，加你1分" 
		    score(sum)
		    win()
	    elif next=="no":
		    win()
	    else:
		    print "不明白你的意思!"
	
def score(sum):
    if sum<=0:
	    print "你分数被扣光了，游戏结束！"
	    exit(0)
    else:
	    print "现在还剩%s分" %sum
		
def win():
    print "恭喜您！安全到达外婆家。"
    exit(0)

start(3)
	