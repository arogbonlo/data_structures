#!/usr/bin/python

"""linkedlist.py
My implementation of linked lists

Author: Xero
Dependencies:
License: Apache v2.0
"""

from operator import eq

__all__ = ["LinkedList", "cons_", "car", "cdr"]


class LinkedList(object):
    """A singly linked list class
    With this linked list, traversal is possible only in the forward direction
    i.e. from head to tail.
    """
    __version__ = "0.1"

    def __init__(self):
        self.terminator = None
        self.head = None
        return None

    def cons(self, value):
        """Push an atom onto the head of a LinkedList"""
        tmp = self.head
        value_cell = ConsCell(value)
        value_cell.next = tmp
        self.head = value_cell
        return self

    def pop(self):
        """Remove the top element from the LinkedList"""
        tmp = self.head
        self.head = tmp.next
        tmp.next = None
        return tmp.value

    def tail(self):
        """Return a LinkedList with the head of self removed"""
        return LinkedList.from_sequence([i for i in self][1:])

    def last(self):
        """Return the last element of the LinkedList"""
        return [i for i in self][-1]

    @classmethod
    def from_sequence(cls, seq):
        """Construct a linked list from a sequence
        Parameters
        ----------
        seq     a sequence like object e.g. list, tuple, string.
                seq must be orderable, this means unordered collections
                such as sets and dictionaries are unsuitable.

        Returns
        -------
        new_linked_list A new LinkedList object.
        """
        # new_linked_list = LinkedList()
        new_list = cls()
        for item in reversed(seq):
            new_list.cons(item)
        return new_list

    @classmethod
    def merge_linked_list(cls, llist_1, llist_2):
        """Return a new linked list gotten by merging 2 linked lists"""
        assert type(llist_1) == type(llist_2), "Both lists must be same kind"
        new_linked_list = cls.from_sequence([i for i in llist_1])
        new_linked_list.last().next = llist_2.head
        return new_linked_list

    @staticmethod
    def car(llist):
        return llist.head

    @staticmethod
    def cdr(llist):
        return llist.tail()

    @staticmethod
    def cons_(atom, llist):
        return llist.cons(atom)

    def __iter__(self):
        val = self.head
        while True:
            if val is None:
                break
            yield val
            val = val.next

    def __repr__(self):
        vals = " ".join(str(i.value) for i in self)
        return "LL({})".format(vals)

    def __len__(self):
        return len([i for i in self.__iter__()])

    def __reversed__(self):
        tmp = LinkedList()
        for i in self:
            tmp.cons(i.value)
        return tmp

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        self_vals = (i.value for i in self)
        other_vals = (i.value for i in other)
        return all(map(lambda x: eq(x[0], x[1]), zip(self_vals, other_vals)))

    def __concat__(self, other):
        return LinkedList.merge_linked_list(self, other)

    def __add__(self, other):
        return self.__concat__(other)


cons_ = LinkedList.cons_
car = LinkedList.car
cdr = LinkedList.cdr


class ConsCell(object):
    """ConsCell class to hold linked list elements"""
    __version__ = "0.1"

    def __init__(self, value):
        self.value = value
        self.next = None
        return None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value
