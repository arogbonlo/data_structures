#!/usr/bin/python

"""stack.py
A class implementing a stack

Author: Xero
Dependencies: 
License: Apache v2.0
"""

class Stack(object):
    """Stack data structure"""
    _version_ = "0.1"

    def __init__(self):
        self.stack = []
        return None


    def peek(self):
        """Return the item at the top of the stack without poping it off."""
        if self.stack == []:
            raise ValueError("Stack empty!")
        return self.stack[-1]


    def push(self, item):
        """Add an item to the top of the stack"""
        self.stack.append(item)
        return None


    def pop(self):
        """Return the item at the top of the stack and take it off the stack
        If the stack is empty, raise an error
        """
        if self.stack:
            return self.stack.pop()
        else:
            raise ValueError("Stack empty, no item to pop!")


    def __len__(self):
        """Return the number of items in the stack"""
        return len(self.stack)
