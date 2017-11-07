7.
class Human:
    name = 'human'

class Bob(Human):
    pass

class Alice(Human):
    pass
Bob.name
 = 'bob'
Human.name
 = 'potato'
print(Human.name
,
Bob.name
, Alice.name)


A. 'potato', 'potato', 'potato'
B. 'potato', 'bob', 'human'
C. 'potato', 'potato', 'human'
D. 'potato', 'bob', 'potato'
