if 1:
    print('hello 1')

a=3
if a>1:
    print('hello 3')

b=5
if b==5:
    print('hello 5')

a=3
if a>4:
    print('hello 4')
else:
    print('hello a')
    
a=5
if a>4:
    print('hello 4')
else:
    print('hello a')
    
a=3
if a>5:
    print('hello 5')
elif a<2:
    print('hello 2')
else:
    print('Tupo hello')
    
a=3
b=4
c=5
if a>3 and b==2:
    print('Good')
elif b>3 or c==5:
    print('Best')
else:
    print('Bad')
    
for i in 1,3,4:
    print(i**2, end=' ')
    print(i**2, sep=' ')
    
a=[1,5,7,10]
for i in a: 
    print(i**3, end=' "Yes" ')

for i in range(0, 10, 1):
    print(i, end=' ') 