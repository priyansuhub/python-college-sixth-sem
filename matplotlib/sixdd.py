import matplotlib.pyplot as plt

list = [10,40,30,34,50,44,15,20]
list1 = [10,40,1,33,52,47,15,70]
# plt.pie(list,labels=list)
# plt.show()
plt.violinplot([list,list1])
plt.show()