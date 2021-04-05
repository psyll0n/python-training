'''
“When a() is called ➎, it calls b() ➊, which in turn calls c() ➌. 
The c() function doesn’t call anything; it just displays c() starts ➍ and c() returns before returning to the line in b() that called it ➌. 
Once execution returns to the code in b() that called c(), it returns to the line in a() that called b() ➊. 
The execution continues to the next line in the b() function ➋, which is a call to d(). Like the c() function, the d() function also doesn’t call anything. 
It just displays d() starts and d() returns before returning to the line in b() that called it. Since b() contains no other code, the execution returns to the line in a() that called b() ➋. The last line in a() displays a() returns before returning to the original a() call at the end of the program ➎.”
'''


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# Excerpt From: Al Sweigart. “Automate the Boring Stuff with Python.” Apple Books. 


