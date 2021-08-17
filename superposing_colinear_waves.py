from numpy import *
import matplotlib.pyplot as p

#print(p.style.available)


a = int(input('How  many waves you want to superpose?\n'))

print("Use 't' as the variable")

c=0
t = linspace(0,2*pi,1000)


for i in range(1,a+1):
    b = eval(input('Give the '+str(i)+' th wave : '))
    p.plot(b,lw='0.9',label='$\phi$('+str(i)+')')
    c = c+b
    
    
#s = input('What kind of graph do you want?\n ')
#print(s,' type graph')
p.style.use('fast')

p.plot(c,'r-',lw='2',label='Resultant Wave')
p.title('Superposition of '+str(a)+' colinear waves')
p.legend()
p.xlabel('$\phi$(x)')
p.ylabel('t')
p.show()



