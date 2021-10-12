#!/usr/bin/env python
# coding: utf-8
##################################################################################################
"""
Exercise #1
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a
particular day. Your task is to print each item_name and net_price in order
of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format
The first line contains the number of items, .
The next  lines contain the item's name and price, separated by a space.

Constraints
N <= 100

Output Format
Print the item_name and net_price in order of its first occurrence.
"""
from collections import OrderedDict

output = OrderedDict()

with open("input_file.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines[1:]:
        count = int(line.split(" ")[-1])
        name = " ".join(line.split(" ")[:-1])
        output[name] = count
        
for name, count in output.items():
    print(name, count)

##################################################################################################
"""
Exercise #2

Rahue is a shoe shop owner. His shop has  X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  N number of customers who are willing to pay xi amount of money only
if they get the shoe of their desired size.
Your task is to compute how much money  Rahue earned.

Input Format
The first line contains X , the number of shoes.
The second line contains a space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired 
by the customer and xi  the price of the shoe. 

Output Format
Print the amount of money earned by Rahue.

"""
from collections import Counter

with open("input_file_2.txt", "r") as f:
    lines = f.read().splitlines()
    sizes = Counter(lines[1].split(" "))
    
    output = sum([Counter({int(a): int(b)}) for a,b in
                  [i.split(" ") for i in lines[4:]] if a in sizes], Counter())
    
    print(sum(output.values()))

##################################################################################################

"""
Exercise #3
Create an iterator that given a filename will return an object that on every iteration
will return a single character. As an option let the user skip newlines, or maybe 
any pre-defined character.
"""
class iter_letters():
    def __init__(self, file_path, skip_char=None):
        self._skip_char = skip_char
        with open(file_path, 'r') as f:
            self._file_data = f.read()
        self._index = 0
    
    def __next__(self):
        
        while True:
            if self._index == len(self._file_data):
                raise StopIteration()
            
            x = self._file_data[self._index]
            self._index += 1
            
            if self._skip_char is not None and x == self._skip_char:
                continue 
        
            return x
            
    def __iter__(self):
        return self

    
a = iter_letters("nice.txt", 'm')
''.join(list(iter(a)))

##################################################################################################

"""
Exercise #4
Create a generator that yields recursively all files paths in a specified 
path (you can use the os or pathlib modules for that).
"""
from pathlib import Path

def path_gen(file_path, skip_char=None):
    skip_char = skip_char
    with open(file_path, 'r') as f:
        file_data = f.read()
    
    for l in file_data:
        if l is not skip_char:
            yield l

''.join(list(path_gen("nice.txt", 'r')))

##################################################################################################

"""
Exercise #5
Write a simple decorator (@hello) that prints “hello world” in every function it decorates
Write a parameterized decorator (@debug) that returns the decorated function 
if and only if the decorator gets a True parameter and a function that 
prints “Debug” otherwise.

"""
import time

def say(text): 
    def _say(func): 
        def call_func(*args, **kwargs):  
            print(text) 
            return func(*args, **kwargs) 
        return call_func 
    return _say

def debug(enabled): 
    def _debug(func): 
        def call_func(*args, **kwargs):  
            a = time.time()
            x = func(*args, **kwargs) 
            b = time.time()
            if enabled:
                print("Function time: {}".format(b-a))
            return x
            
        return call_func 
    return _debug


DEBUG = False

@say("Hello")
@debug(DEBUG)
def add(a,b,c):
    return a+b+c

@debug(DEBUG)
def break_sha1(a):
    time.sleep(4)

add(1,2,3)

##################################################################################################