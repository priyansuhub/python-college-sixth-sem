#Create a simple list
import pandas as pd
priceList =[100,200,300,400]
#Create a Series
productSeries =  pd.Series(priceList, index=['Pen','Shirt','Deo','Pant'])
print(productSeries)
#Create A data frame
productPd = pd.DataFrame([[1,2,3,4,5],[6,7,5,4,3]], columns=['Lala','Bala','Mala','Nala','Kala'])
print(productPd)
print(productPd.size)
print(productPd.shape)
print(productPd.keys())
#Add rows and columns in a dataframe
productPd2 = pd.DataFrame([[2,3,4,5,6],[1,2,9,7,6]], columns=['Lala','Bala','Mala','Nala','Kala'] )
product3 = productPd.append(productPd2)
print(product3) 
product3["Haha"] = [5,6,7,8]
print(product3)
#Deleting rows from dataFrame
product3 =product3.drop(index=[0])
print(product3)
