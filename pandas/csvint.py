import pandas as pd
# import csv data
data = pd.read_csv("/home/priyansu/pythontest/pandas/vgsales.csv")

def basic():
    print(data.size)
    print(data.shape)
    print(data.keys())
    # describe(), info(), head(), tail()
    # Describe aapka stastical info dikhata hai
    print(data.describe())
    # info aapka datatype wagera 
    print(data.info())
    # Head first five details
    print(data.head())
    # Tail last five details
    print(data.tail())
    # values
    print(data[['Rank','Platform']].values)
    # =========================================
    # =========================================
    # print all the value count of Platform
    print(data['Platform'].value_counts())
    # Percentage
    print(data['Platform'].value_counts()/len(data['Platform']))
    # tolist() bhi hai ek
    # =========================================
    # =========================================
    # mean median max min sum product maaro ab
    # nsmallest and nlargest
#Sort functions
def thodaAdvance():
    print(data.sort_values(by='Global_Sales').tail(3))
    newdata = data[data['Platform'] == 'Wii']
    print(newdata.head(3))
    print(data.iloc[3,9])
    #get all columns of a specific row
    print(data.iloc[2])
    print(data.iloc[[3,4],[4,8]])
    #6th column, 2 sai 9 rows
    print(data.iloc[2:9,[6]])

def ilocKaUlta():
    print(data.loc[1:3,'Rank':'Year'])
ilocKaUlta()