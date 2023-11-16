#!/usr/bin/env python3

from index import (capital_fruit, reversed_fruit, unspaced_fruit, upversed_fruit, inauguration_dates, say_names, get_dogs, get_evens, squared_numbers, summed_lists)

# import io
# import sys

class TestListComprehension:
    '''Add your list comprehensions in index.py'''

    def test_capital_fruit(self):
        '''capital_fruit() returns a new list of capitalized fruits.'''
        assert(capital_fruit() == ["Banana", "Apple", "Orange", "Kiwi", "Kumquat"])

    def test_reversed_fruit(self):
        '''reversed_fruit() returns a new list of reversed fruits.'''
        assert(reversed_fruit() == ["ananab", "elppa", "egnaro", "iwik", "hsauqs"])

    def test_unspaced_fruit(self):
        '''unspaced_fruit() returns a new list of fruits without whitespaces'''
        assert(unspaced_fruit() == ["banana", "apple", "orange", "kiwi", "starfruit"])

    def test_upversed_fruit(self):
        '''upversed_fruit() returns a list of fruits upcased and reversed'''
        assert(upversed_fruit() == ["ANANAB", "ELPPA", "EGNARO", "IWIK", "HCAEP"])

    def test_inauguration_dates(self):
        '''inauguration_dates() returns a new list of inauguration dates by president'''
        assert(inauguration_dates() == [1789, 1797, 1801, 1809, 1817])

    def test_say_names(self):
        '''say_names() returns a list of concatenated names'''
        assert(say_names() == ["Chett Tiller", "Ricardo Guerra", "Charlie Kozie", "Alina Pisarenko", "Aakash Sudhakar", "Sakib Rasul", "Daniel Gaston", "Ben Cavins", "Mohammad Hossain", "Chelsea Green"])

    def test_get_dogs(self):
        '''get_dogs() returns a list of only dogs with the cats filtered out'''
        assert(get_dogs() == ["dog", "dog", "dog", "dog", "dog"])

    def test_get_evens(self):
        '''get_evens() returns a list of only even numbers'''
        assert(get_evens() == [8,16,20])

    def test_squared_numbers(self):
        '''squared_numbers() returns each number in the range squared'''
        assert(squared_numbers() == [1,4,9,16,25,36,49,64,81])

    def test_summed_lists(self):
        '''summed_lists() returns the sum of each of the nested lists'''
        assert(summed_lists() == [15,35,0,42])