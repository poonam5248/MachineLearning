Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    plt.plot(x,y)
NameError: name 'x' is not defined
>>> x=[2,4,5,8]
>>> y=[5,6,7,8]
>>> import matplot.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import matplot.pyplot as plt
ModuleNotFoundError: No module named 'matplot'
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000189AE648860>]
>>> p=[2,3,4,5]
>>> q=[7,8,9,10]
>>> plt.plot(x,y,p,q)
[<matplotlib.lines.Line2D object at 0x00000189ABA030B8>, <matplotlib.lines.Line2D object at 0x00000189AE648E80>]
>>> plt.show()
