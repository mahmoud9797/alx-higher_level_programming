#!/usr/bin/pythn3
def multiply_by_2(a_dictionary):
   new_dic = {}
   for key, value in a_dictionary.items():
       new_dic[key] = (lambda x: x * 2)(value)
   return new_dic

