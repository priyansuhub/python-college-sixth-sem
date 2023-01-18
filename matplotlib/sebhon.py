import matplotlib.pyplot as plt
import numpy as np

ecommerce = ['Myntra','Snapdeal','Alibaba','Amazon','Flipkart']
profit1=[35,45,100,70,40]
profit2=[25,35,40,60,80]
profit3=[15,25,50,79,47]
profit4=[5,53,69,19,26]

# plt.figure(1,figsize=(10,10))
# plt.subplot(221)
# plt.bar(ecommerce,profit1)

# plt.subplot(222)
# plt.bar(ecommerce,profit2)

# plt.subplot(223)
# plt.bar(ecommerce,profit3)

# plt.subplot(224)
# plt.bar(ecommerce,profit4)

M,N = np.mgrid[10:20, 10:15]
print(M)
print(N)
# plt.quiver(M,N)
# plt.show()
