Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
d
>>> d=pd.DataFrame([5,2,4,8])
>>> print(d)
   0
0  5
1  2
2  4
3  8
>>> print(d[1])
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 987, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 993, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(d[1])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 987, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 993, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 1
>>> d[0]
0    5
1    2
2    4
3    8
Name: 0, dtype: int64
>>> d=pd.DataFrame({a:[5,2,4,8})
		   
SyntaxError: invalid syntax
>>> d=pd.DataFrame({a:[5,2,4,8]})
		   
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d=pd.DataFrame({a:[5,2,4,8]})
NameError: name 'a' is not defined
>>> d=pd.DataFrame({0:[5,2,4,8]})
		   
>>> d=pd.DataFrame({'a':[5,2,4,8]})
		   
>>> d
		   
   a
0  5
1  2
2  4
3  8
>>> d['a'][1]
		   
2
>>> d=pd.DataFrame({'a':[5,2,4,8],'b':[4,8,5,2]})
		   
>>> d
		   
   a  b
0  5  4
1  2  8
2  4  5
3  8  2
>>> d['a'[1]['b'][1]
d
      
SyntaxError: invalid syntax
>>> d['a','b'][1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 'b')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d['a','b'][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 'b')
>>> d[['a','b']][1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d[['a','b']][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> d[{'a','b'}][1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[{'a','b'}][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> d['a'][1]
      
2
>>> d['b'][1]
      
8
>>> d['a',1]['b',1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 1)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d['a',1]['b',1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 1)
>>> d[['a'[1],'b'[1]]]
      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[['a'[1],'b'[1]]]
IndexError: string index out of range
>>> d[['a','b'[1]]]
      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[['a','b'[1]]]
IndexError: string index out of range
>>> d[{'a','b'}][1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d[{'a','b'}][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> D=d.T
      
>>> D
      
   0  1  2  3
a  5  2  4  8
b  4  8  5  2
>>> D[1]
      
a    2
b    8
Name: 1, dtype: int64
>>> d.shape
      
(4, 2)
>>> d.ndim
      
2
>>> d.size
      
8
>>> D.shape
      
(2, 4)
>>> D.size
      
8
>>> D.ndim
      
2
>>> d=pd.DataFrame[[5,2,4,8],[4,8,5,2]]
      
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d=pd.DataFrame[[5,2,4,8],[4,8,5,2]]
TypeError: 'type' object is not subscriptable
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]])
      
>>> d
      
   0  1  2  3
0  5  2  4  8
1  4  8  5  2
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],column=['a','b'])
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],column=['a','b'])
TypeError: __init__() got an unexpected keyword argument 'column'
>>> d[1:2]
      
   0  1  2  3
1  4  8  5  2
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],column=['a','b'],index=['c','d'])
      
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],column=['a','b'],index=['c','d'])
TypeError: __init__() got an unexpected keyword argument 'column'
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]]index=['c','d'])
      
SyntaxError: invalid syntax
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],index=['c','d'])
      
>>> d
      
   0  1  2  3
c  5  2  4  8
d  4  8  5  2
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'])
      
>>> d
      
   a  b  c  d
0  5  2  4  8
1  4  8  5  2
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b'])
      
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b'])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 435, in __init__
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 404, in to_arrays
    dtype=dtype)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 436, in _list_to_arrays
    coerce_float=coerce_float)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 492, in _convert_object_array
    con=len(content)))
AssertionError: 2 columns passed, passed data had 4 columns
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'])
>>> d
   a  b  c  d
0  5  2  4  8
1  4  8  5  2
>>> d=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['abc','def'])
>>> d
     a  b  c  d
abc  5  2  4  8
def  4  8  5  2
>>> d['abc']['b']
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d['abc']['b']
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'
>>> d['abc']['b'][1]
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d['abc']['b'][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'
>>> d['abc'][1]
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d['abc'][1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'
>>> d['b'][1]
8
>>> d['b'][0]
2
>>> d['c'][0]
4
>>> d['c'][1]
5
>>> d[['b','c']]
     b  c
abc  2  4
def  8  5
>>> d['e']=d['c']+d['d']
>>> d
     a  b  c  d   e
abc  5  2  4  8  12
def  4  8  5  2   7
>>> m=d[{'a','b'}]
>>> m
     b  a
abc  2  5
def  8  4
>>> type(m)
<class 'pandas.core.frame.DataFrame'>
>>> d[:]
     a  b  c  d   e
abc  5  2  4  8  12
def  4  8  5  2   7
>>> d[1]
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d[1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 1
>>> d[:]['abc']
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d[:]['abc']
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'
>>> d[0:1]['abc']
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    d[0:1]['abc']
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'abc'
>>> d[0:1]
     a  b  c  d   e
abc  5  2  4  8  12
>>> d.ndim
2
>>> d.shape
(2, 5)
>>> d[1:2]
     a  b  c  d  e
def  4  8  5  2  7
>>> d['a'][0:1]
abc    5
Name: a, dtype: int64
>>> d['a][0:2]
      
SyntaxError: EOL while scanning string literal
>>> d['a'][0:2]
      
abc    5
def    4
Name: a, dtype: int64
>>> d['a'][0:1]
      
abc    5
Name: a, dtype: int64
>>> d['a','b'][0:1]
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 'b')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    d['a','b'][0:1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('a', 'b')
>>> d['a':'b'][0:1]
      
     a  b  c  d   e
abc  5  2  4  8  12
>>> d[0:2][0:1]
      
     a  b  c  d   e
abc  5  2  4  8  12
>>> d[{'a','b'}][0:1]
      
     b  a
abc  2  5
>>> d[['a','b']][0:1]
      
     a  b
abc  5  2
>>> d.T
      
   abc  def
a    5    4
b    2    8
c    4    5
d    8    2
e   12    7
>>> d.T
      
   abc  def
a    5    4
b    2    8
c    4    5
d    8    2
e   12    7
>>> d.sum()
      
a     9
b    10
c     9
d    10
e    19
dtype: int64
>>> d.add(d1,d2)
      
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d.add(d1,d2)
NameError: name 'd1' is not defined
>>> d1=pd.DataFrame([5,2,4,8],[4,8,5,2])
      
>>> d1
      
   0
4  5
8  2
5  4
2  8
>>> d2=pd.DataFrame([5,2,4,8],[4,8,5,2])
      
>>> d2
      
   0
4  5
8  2
5  4
2  8
>>> d2=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'],index=['abc','def'])
      
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d2=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'],index=['abc','def'])
TypeError: __init__() got multiple values for argument 'index'
>>> d1=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'])
      
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1651, in create_block_manager_from_blocks
    placement=slice(0, len(axes[0])))]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\blocks.py", line 3095, in make_block
    return klass(values, ndim=ndim, placement=placement)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\blocks.py", line 87, in __init__
    '{mgr}'.format(val=len(self.values), mgr=len(self.mgr_locs)))
ValueError: Wrong number of items passed 1, placement implies 4

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d1=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 451, in __init__
    copy=copy)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 167, in init_ndarray
    return create_block_manager_from_blocks([values], [columns, index])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1660, in create_block_manager_from_blocks
    construction_error(tot_items, blocks[0].shape[1:], axes, e)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1691, in construction_error
    passed, implied))
ValueError: Shape of passed values is (4, 1), indices imply (4, 4)
>>> d.T
   abc  def
a    5    4
b    2    8
c    4    5
d    8    2
e   12    7
>>> d1.T
   4  8  5  2
0  5  2  4  8
>>> d1=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'],index=['abc','def'])
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d1=pd.DataFrame([5,2,4,8],[4,8,5,2],columns=['a','b','c','d'],index=['abc','def'])
TypeError: __init__() got multiple values for argument 'index'
>>> d.T
   abc  def
a    5    4
b    2    8
c    4    5
d    8    2
e   12    7
>>> d1.T
   4  8  5  2
0  5  2  4  8
>>> d2.T
   4  8  5  2
0  5  2  4  8
>>> d.add(d1,d2)
      a   b   c   d   e   0
2   NaN NaN NaN NaN NaN NaN
4   NaN NaN NaN NaN NaN NaN
5   NaN NaN NaN NaN NaN NaN
8   NaN NaN NaN NaN NaN NaN
abc NaN NaN NaN NaN NaN NaN
def NaN NaN NaN NaN NaN NaN
>>> d2=pd.DataFrame([5,2,4,8],[4,8,5,2])
>>> d2
   0
4  5
8  2
5  4
2  8
>>> d.add(d1,d2)
      a   b   c   d   e   0
2   NaN NaN NaN NaN NaN NaN
4   NaN NaN NaN NaN NaN NaN
5   NaN NaN NaN NaN NaN NaN
8   NaN NaN NaN NaN NaN NaN
abc NaN NaN NaN NaN NaN NaN
def NaN NaN NaN NaN NaN NaN
>>> import numpy as np
>>> a=np.array(50).reshape(5,10)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a=np.array(50).reshape(5,10)
ValueError: cannot reshape array of size 1 into shape (5,10)
>>> import numpy as np
>>> import pandas as pd
>>> a=np.arange(50).reshape(5,10)
>>> d=pd.DataFrame(a)
>>> d
    0   1   2   3   4   5   6   7   8   9
0   0   1   2   3   4   5   6   7   8   9
1  10  11  12  13  14  15  16  17  18  19
2  20  21  22  23  24  25  26  27  28  29
3  30  31  32  33  34  35  36  37  38  39
4  40  41  42  43  44  45  46  47  48  49
>>> d=pd.DataFrame(a,columns=['a','b','c','d','e','f','g','h','i','j'])
>>> d
    a   b   c   d   e   f   g   h   i   j
0   0   1   2   3   4   5   6   7   8   9
1  10  11  12  13  14  15  16  17  18  19
2  20  21  22  23  24  25  26  27  28  29
3  30  31  32  33  34  35  36  37  38  39
4  40  41  42  43  44  45  46  47  48  49
>>> d=pd.DataFrame(a,columns=['a','b','c','d','e','f','g','h','i','j'],index=['a','b','c','d','e'])
>>> d
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> d['b','c'][0:2]
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('b', 'c')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    d['b','c'][0:2]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('b', 'c')
>>> d[['b','c']][0:2]
    b   c
a   1   2
b  11  12
>>> d[['b','c']][['a','b']]
d
SyntaxError: multiple statements found while compiling a single statement
>>> d[['b','c']][['a','b']]

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    d[['b','c']][['a','b']]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2934, in __getitem__
    raise_missing=True)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1354, in _convert_to_indexer
    return self._get_listlike_indexer(obj, axis, **kwargs)[1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1161, in _get_listlike_indexer
    raise_missing=raise_missing)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1252, in _validate_read_indexer
    raise KeyError("{} not in index".format(not_found))
KeyError: "['a'] not in index"
>>> d[['b','c']][0:]
    b   c
a   1   2
b  11  12
c  21  22
d  31  32
e  41  42
>>> d[['b','c']][0:4]
    b   c
a   1   2
b  11  12
c  21  22
d  31  32
>>> d[['b','c']][0:2].sum()
b    12
c    14
dtype: int64
>>> d[['b','c']][0:2]=temp
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    d[['b','c']][0:2]=temp
NameError: name 'temp' is not defined
>>> e=d[['b','c']][0:2]
>>> e=d[['i','j']][8:9]
>>> e
Empty DataFrame
Columns: [i, j]
Index: []
>>> e=d[['i','j']][7:9]
>>> e
Empty DataFrame
Columns: [i, j]
Index: []
>>> e=d[['b','c']][0:2]
>>> e
    b   c
a   1   2
b  11  12
>>> d[['b','c']][0:2].sum()
b    12
c    14
dtype: int64
>>> e=d[['b','c']][3:4]
>>> e
    b   c
d  31  32
>>> e=d[['b','c']][3:9]
>>> e
    b   c
d  31  32
e  41  42
>>> e=d[['i','j']][3:9]
>>> e
    i   j
d  38  39
e  48  49
>>> d[['b','c']][0:2]=e

Warning (from warnings module):
  File "__main__", line 1
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy

Warning (from warnings module):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3374
    self.loc._setitem_with_indexer(key, value)
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy

Warning (from warnings module):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 3362
    return self._setitem_slice(indexer, value)
SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
e
>>> d[['b','c']][0:2]
    b   c
a   1   2
b  11  12
>>> e=d[['i','j']][3:9]
>>> e
    i   j
d  38  39
e  48  49
>>> d[['b','c']][0:2]=d[['i','j']][3:9]
>>> d
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> e
    i   j
d  38  39
e  48  49
>>> e=f
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    e=f
NameError: name 'f' is not defined
>>> f=e
>>> f
    i   j
d  38  39
e  48  49
>>> g=d
>>> d
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> aa=d[['b','c']][0:2]
>>> aa
    b   c
a   1   2
b  11  12
>>> bb=d[['i','j']][3:9]
>>> bb
    i   j
d  38  39
e  48  49
>>> temp=aa
>>> aa=bb
>>> bb=temp
>>> aa
    i   j
d  38  39
e  48  49
>>> bb
    b   c
a   1   2
b  11  12
>>> d
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> temp
    b   c
a   1   2
b  11  12
>>> d[[aa','bb']][0:2]
       
SyntaxError: invalid syntax
>>> d[['aa','bb']][0:2]
       
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    d[['aa','bb']][0:2]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2934, in __getitem__
    raise_missing=True)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1354, in _convert_to_indexer
    return self._get_listlike_indexer(obj, axis, **kwargs)[1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1161, in _get_listlike_indexer
    raise_missing=raise_missing)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1246, in _validate_read_indexer
    key=key, axis=self.obj._get_axis_name(axis)))
KeyError: "None of [Index(['aa', 'bb'], dtype='object')] are in the [columns]"
>>> d[['b','c']]['aa','bb']
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('aa', 'bb')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    d[['b','c']]['aa','bb']
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2927, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: ('aa', 'bb')
>>> aa
    i   j
d  38  39
e  48  49
>>> bb
    b   c
a   1   2
b  11  12
>>> d[['b','c']][0:2]==aa
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    d[['b','c']][0:2]==aa
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\ops.py", line 2096, in f
    raise ValueError('Can only compare identically-labeled '
ValueError: Can only compare identically-labeled DataFrame objects
>>> d[['b','c']][0:2]=aa
		     
>>> d
		     
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> d[['i','j']][3:9]=bb
		     
>>> d
		     
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> d[['b','c']][0:2]=aa
		     
>>> a
		     
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])
>>> d
		     
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> aa
		     
    i   j
d  38  39
e  48  49
>>> bb
		     
    b   c
a   1   2
b  11  12
>>> m=d[['b','c']][0:2]
		     
>>> m
		     
    b   c
a   1   2
b  11  12
>>> n=d[['i','j']][3:5]
		     
>>> n
		     
    i   j
d  38  39
e  48  49
>>> d[['b','c']][0:2]=n
		     
>>> d
		     
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> n
		     
    i   j
d  38  39
e  48  49
>>> d[['b','c']][0:2]=n[['b','c']][0:2]
		     
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    d[['b','c']][0:2]=n[['b','c']][0:2]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 2934, in __getitem__
    raise_missing=True)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1354, in _convert_to_indexer
    return self._get_listlike_indexer(obj, axis, **kwargs)[1]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1161, in _get_listlike_indexer
    raise_missing=raise_missing)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1246, in _validate_read_indexer
    key=key, axis=self.obj._get_axis_name(axis)))
KeyError: "None of [Index(['b', 'c'], dtype='object')] are in the [columns]"
>>> d[columns]
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    d[columns]
NameError: name 'columns' is not defined
>>> d[[columns]]
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    d[[columns]]
NameError: name 'columns' is not defined
>>> d.columns
Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], dtype='object')
>>> d.index
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
>>> d.iloc(0)
<pandas.core.indexing._iLocIndexer object at 0x0000021744D7D098>
>>> d[0:1]
   a  b  c  d  e  f  g  h  i  j
a  0  1  2  3  4  5  6  7  8  9
>>> d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['a','b','c','d'])
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1667, in create_block_manager_from_arrays
    mgr = BlockManager(blocks, axes)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 114, in __init__
    self._verify_integrity()
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 311, in _verify_integrity
    construction_error(tot_items, block.shape[1:], self.axes)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1691, in construction_error
    passed, implied))
ValueError: Shape of passed values is (2, 4), indices imply (4, 4)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['a','b','c','d'])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 448, in __init__
    dtype=dtype)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 61, in arrays_to_mgr
    return create_block_manager_from_arrays(arrays, arr_names, axes)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1671, in create_block_manager_from_arrays
    construction_error(len(arrays), arrays[0].shape, axes, e)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\managers.py", line 1691, in construction_error
    passed, implied))
ValueError: Shape of passed values is (2, 4), indices imply (4, 4)
>>> d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b'],index=['a','b','c','d'])
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b'],index=['a','b','c','d'])
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\frame.py", line 435, in __init__
    arrays, columns = to_arrays(data, columns, dtype=dtype)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 404, in to_arrays
    dtype=dtype)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 436, in _list_to_arrays
    coerce_float=coerce_float)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\internals\construction.py", line 492, in _convert_object_array
    con=len(content)))
AssertionError: 2 columns passed, passed data had 4 columns
>>> d1=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['a','b'])
>>> d1
   a  b  c  d
a  5  2  4  8
b  4  8  5  2
>>> d2=pd.DataFrame([[5,2,4,8],[4,8,5,2]],columns=['a','b','c','d'],index=['a','b'])
>>> d2
   a  b  c  d
a  5  2  4  8
b  4  8  5  2
>>> d.add(d1,d2)
      a     b     c     d   e   f   g   h   i   j
a   5.0   3.0   6.0  11.0 NaN NaN NaN NaN NaN NaN
b  14.0  19.0  17.0  15.0 NaN NaN NaN NaN NaN NaN
c   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
d   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
e   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
>>> q.add(d1,d2)
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    q.add(d1,d2)
NameError: name 'q' is not defined
>>> s=d.add(d1,d2)
>>> s
      a     b     c     d   e   f   g   h   i   j
a   5.0   3.0   6.0  11.0 NaN NaN NaN NaN NaN NaN
b  14.0  19.0  17.0  15.0 NaN NaN NaN NaN NaN NaN
c   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
d   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
e   NaN   NaN   NaN   NaN NaN NaN NaN NaN NaN NaN
>>> m.columns
Index(['b', 'c'], dtype='object')
>>> n.columns
Index(['i', 'j'], dtype='object')
>>> m.columns[[i,j]]
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    m.columns[[i,j]]
NameError: name 'i' is not defined
>>> m.columns[['i','j']]

Warning (from warnings module):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3969
    result = getitem(key)
FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    m.columns[['i','j']]
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 3969, in __getitem__
    result = getitem(key)
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
>>> m.columns=[['i','j']]
>>> m
    i   j
a   1   2
b  11  12
>>> n=columns=[['b','c']]
>>> n
[['b', 'c']]
>>> n.columns=[['b','c']]
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    n.columns=[['b','c']]
AttributeError: 'list' object has no attribute 'columns'
>>> n.columns=[['b','c']]
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    n.columns=[['b','c']]
AttributeError: 'list' object has no attribute 'columns'
>>> d.loc['i']
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2657, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'i'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    d.loc['i']
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1500, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 1913, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexing.py", line 141, in _get_label
    return self.obj._xs(label, axis=axis)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 3585, in xs
    loc = self.index.get_loc(key)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\indexes\base.py", line 2659, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 108, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1601, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1608, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'i'
>>> d.iloc[0:3]
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
>>> d
    a   b   c   d   e   f   g   h   i   j
a   0   1   2   3   4   5   6   7   8   9
b  10  11  12  13  14  15  16  17  18  19
c  20  21  22  23  24  25  26  27  28  29
d  30  31  32  33  34  35  36  37  38  39
e  40  41  42  43  44  45  46  47  48  49
>>> 
