#!/usr/bin/env python3
# python_class_inheritance2.py - Script that showcases the concept of class inheritance in Python.

class Parent(object):
    def spam(self):
        print('Parent.spam')

class A(Parent):
    def spam(self):
        print('A.spam')
        super().spam()


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()


class D(Parent):
    def spam(self):
        print('D.spam')