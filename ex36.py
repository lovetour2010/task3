# -*- coding: utf-8 -*-
from sys import exit
def start(sum):
    print '''
	Welcome!
	��ʼ����3�֣�����Ϸ�����У��������Ϊ0�������˳���Ϸ��
	�����ǿ�ʼ�ɣ�
	����������ȥ���ŵ����С·�ϡ�
	Oh��ǰ���и���Ģ�����Ƿ�Ҫ��ժ��ע�⣺���ܻ��ж�Ŷ����������\'yes\' ���� \'no\': '''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum-1
		    print "�浹ù����Ģ���ж������Ѿ�����1����" 
		    score(sum)
		    boat(sum)
	    elif next=="no":
		    print "������ǰ�߰ɡ���"
		    boat(sum)
	    else:
		    print "�����������˼!"
	   
def boat(sum):
    print '''
    Oh��ǰ�������ӣ�����������԰����Щ��������Ҫ����1�֣�Ҳ����ѡ�������·��
    �Ƿ�Ҫ������������\'yes\' ���� \'no\': '''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum-1
		    print "������1��" 
		    score(sum)
		    fish(sum)
	    elif next=="no":
		    print "������ǰ�߰ɡ���"
		    road(sum)
	    else:
		    print "�����������˼!"
	
def fish(sum):
    print '''���ϴ��о�����ɣ������кܶ��㣬��ֻ����һ�֡�
    ��Ҫ�̺�ɫ�Ļ�����ɫ���㣿������\'red\' ���� \'blue\':'''
	
    while True:
	    next=raw_input(">")
	    if next=="red":
		    sum=sum-1
		    print "�ǳ��ź��������ж����㱻����1��" 
		    score(sum)
		    win()
	    elif next=="blue":
		    print "���������1�֣����ڻ�ʣ%s��" %sum
		    win()
	    else:
		    print "�����������˼!"
	
def road(sum):
    print '''�и������������߹�����ԭ����������·��ע��:������ƭ��Ŷ����
    �Ƿ�Ҫָ·��������\'yes\' ���� \'no\':'''
	
    while True:
	    next=raw_input(">")
	    if next=="yes":
		    sum=sum+1
		    print "�ĳ���������1��" 
		    score(sum)
		    win()
	    elif next=="no":
		    win()
	    else:
		    print "�����������˼!"
	
def score(sum):
    if sum<=0:
	    print "��������۹��ˣ���Ϸ������"
	    exit(0)
    else:
	    print "���ڻ�ʣ%s��" %sum
		
def win():
    print "��ϲ������ȫ�������żҡ�"
    exit(0)

start(3)
	