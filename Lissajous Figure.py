import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,1,1000)
wt = 2*np.pi*t
phi = np.linspace(0,np.pi,500)
print('What is the Frequency ratio(m:n) ?')
m = eval(input('Enter m: '))
n = eval(input('Enter n: '))
a = eval(input('Amplitube of 1st wave: '))
b = eval(input('Amplitube of 2nd wave: '))
for alpha in phi:
    x = a*np.sin(m*wt)
    y = b*np.sin(n*wt-alpha)
    plt.axes().set_aspect('equal')
    plt.plot(x,y,lw=2)
    plt.title('Lissajous Figure\nFrequency ratio '+str(m)+':'+str(n))
    plt.xlim(-5.0,5.0)
    plt.ylim(-5.0,5.0)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()