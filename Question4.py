4.
s1 = set(type('3'), type(2), type(1L), type(0.0))
s2 = set('3'.__class__, 2.__class__, 1L.__class__, 0.0.__class__)

print(s1 == s2)



'''
A. AttributeError
B. True
C. False
D. Ничего из вышеперечисленного
'''



'''
Invalid syntax @ type(1L)
'''
