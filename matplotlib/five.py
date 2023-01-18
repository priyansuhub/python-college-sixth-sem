import matplotlib.pyplot as plt

a = list(range(1,11))
b = list(range(5,55,5))
c = list(range(10,110,10))
d = list(range(20,210,20))

plt.plot(a,a,'g^',a,b,'bs',a,c,'r--',a,d,'mo')
plt.grid(True,color='k')
plt.show()