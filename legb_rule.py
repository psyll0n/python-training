#!/usr/bin/env python3
# Local, enclosing, global, built-in scope rule example.
g = 'global'

def outer(p='param'):
    l = 'local'
    def inner():
        print(g, p, l)
    inner()
    
if __name__ == '__main__':
    outer()
