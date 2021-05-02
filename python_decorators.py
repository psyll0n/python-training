#!/usr/bin/env python3

"""
Simple Click example...
"""

import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do you want to greet?')
@click.option('--name', default='Tammy')

def greet(greeting, name):
    print(f"{greeting} {name}")
    

if __name__ == '__main__':
    greet()