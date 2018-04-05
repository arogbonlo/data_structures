#!/usr/bin/python

"""typed_linkedlist.py
An implementation of typed linked lists akin to Haskell Lists.

Author: Xero
Dependencies: 
License: Apache v2.0
"""

from linked_list import LinkedList

class TypedLinkedList(LinkedList):
    """A singly linkedlist in which every element except the terminator have
    the same type. Strict typing allows functionality such as sorting.

    Numeric types: int and float are allowed in the same list.
    If a float is Consed onto a list of ints, the list becomes a list of floats
    e.g.
    >>> xs = TypedLinkedList()
    >>> for i in range(5): xs.cons(i)
    >>> xs
    int LL(4, 3, 2, 1, 0)
    >>> xs.cons(5.0)
    >>> xs
    float LL(5.0, 4.0, 3.0, 2.0, 1.0, 0.0)
    """
    def __init__(self):
        super().__init__()
        self.type = None
        return None

    def cons(self, value):
        """push an atom onto the head of the list ensuring all the elements of
        the list have the same type.

        An empty TypedLinkedList has type None. The type of elements is can hold
        is determined by the type of the first atom consed onto it.

        Numeric types can be coerced in the following manner:
            If a float is consed onto a list of ints, the list becomes a list of
            floats.

        Parameters
        ----------
        self        an instance of TypedLinkedList
        value       the element to be pushed onto the head of the list

        Returns
        -------
        NoneType

        Raises
        ------
        TypeError   If the type of atom is not the same as the type of the list
        """
        val_type = type(value)
        if not self:
            super().cons(value)
            self.type = val_type
        elif val_type == self.type:
            super().cons(value)
        elif val_type == int and self.type == float:
            value = float(value)
            super().cons(value)
        elif val_type == float and self.type == int:
            for val in self:
                val.value = float(val.value)
            self.type = val_type
            super().cons(value)
        else:
            raise TypeError("{} != {}, All elements in {} must be of the same\
                            type".format(val_type, self.type,
                                         self.__class__.__name__))
        return None

    def __repr__(self):
        vals = " ".join(str(i.value) for i in self)
        return "{} TLL({})".format(self.type, vals)

    def __reversed__(self):
        return self.from_sequence([i.value for i in super().__reversed__()])

    def __concat__(self, other):
        assert self.type == other.type
        return TypedLinkedList.merge_linked_list(self, other)
