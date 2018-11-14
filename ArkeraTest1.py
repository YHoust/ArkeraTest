"""
@author: Yahel
"""

from unittest import TestCase

#What i have changed here is to create a copy of the dictionary
#Since everytime we call the method in ddd we are
#calling the dictionary we have just changed

def increment_dictionary_values(d,i):
    copy = dict(d)
    for k ,v in copy.items():
        copy[k] = v + i
    return copy

class TestIncrementDictionaryValues(TestCase):
       
    def test_increment_dictionary_values(self):
        d = {'a':1}
        dd = increment_dictionary_values(d,1)
        ddd = increment_dictionary_values(d,-1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)

if __name__ == "__main__":
    d = {'a':1}        
    dd = increment_dictionary_values(d,1)
    
    for k,v in dd.items():
        print(k,v)
        
    ddd = increment_dictionary_values(d,-1)
    for k,v in ddd.items(): 
        print(k,v)