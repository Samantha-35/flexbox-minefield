#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: YOUR NAME HERE

:date: 


"""
    
class Cell():
    
    def __init__(self):
        """
        :return: a new hidden cell of a minesweeper's grid.
                 existence of a bomb, number of bombs in neighborhood
                 have to be stated later.
        :rtype: Cell
        :UC: none
        :Examples:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.is_hypothetic()
        False
        >>> cel.is_revealed()
        False
        >>> cel.number_of_bombs_in_neighborhood()
        0
        """

    def is_revealed(self):
        """
        :return: True if self is revealed, False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_revealed()
        False
        >>> cel.reveal()
        >>> cel.is_revealed()
        True
        """


    def reveal(self):
        """
        :return: None
        :side effect: modify reveal state of self
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_revealed()
        False
        >>> cel.reveal()
        >>> cel.is_revealed()
        True
        """

        
    def is_bomb(self):
        """
        :return: True if self contains a bomb, False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.set_bomb()
        >>> cel.is_bomb()
        True
        """

    
    def set_bomb(self):
        """
        :return: None
        :side effect: put a bomb in self 
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_bomb()
        False
        >>> cel.set_bomb()
        >>> cel.is_bomb()
        True
        """

    def is_hypothetic(self):
        """
        :return: True if cel if hypothetically containing a bomb
                 False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        """
    
    def set_hypothetic(self):
        """
        :return: None
        :side effect: modify hypothetic bomb state of self if self is not revealed
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        """

    def unset_hypothetic(self):
        """
        :return: None
        :side effect: modify hypothetic bomb state of self if self is not revealed
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.is_hypothetic()
        False
        >>> cel.set_hypothetic()
        >>> cel.is_hypothetic()
        True
        >>> cel.unset_hypothetic()
        >>> cel.is_hypothetic()
        False
        """


    def number_of_bombs_in_neighborhood(self):
        """
        :return: number of bombs in the neighborhood of self
        :rtype: int
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.number_of_bombs_in_neighborhood()
        0
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> cel.number_of_bombs_in_neighborhood()
        1
        """

        
    def incr_number_of_bombs_in_neighborhood(self):
        """
        :return: None
        :side effect: increment the number of bombs in neighborhood of self
        :UC: none
        :Example:

        >>> cel = Cell()
        >>> cel.number_of_bombs_in_neighborhood()
        0
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> cel.number_of_bombs_in_neighborhood()
        1
        """
    def __str__(self):
        """
        :return: a string representation of self state
        :rtype: str
        :UC: none
        :Example:
        
        >>> cel = Cell()
        >>> str(cel) == ' '
        True
        >>> cel.set_hypothetic()
        >>> str(cel) == '?'
        True
        >>> cel.unset_hypothetic()
        >>> cel.reveal()
        >>> str(cel) == '0'
        True
        >>> cel.incr_number_of_bombs_in_neighborhood()
        >>> str(cel) == '1'
        True
        >>> cel.set_bomb()
        >>> str(cel) == 'B'
        True
        """
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
