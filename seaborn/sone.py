import seaborn
import matplotlib.pyplot as plt
titanic = seaborn.load_dataset('titanic')
def titanicData():
    print(titanic.keys())
    print(titanic.shape)
    print(titanic.describe())
    print(titanic['embarked'])

def plotKaroThoda():
    seaborn.boxplot(x=titanic['class'],y=titanic['fare'],hue=titanic['sex'],data=titanic).set_title('Lmao')
    plt.show()

def plotKaroViolinKo():
    seaborn.violinplot(x=titanic['class'],y=titanic['age'],hue=titanic['sex']).set_title('Lmao')
    plt.show()

# def lineChartPlot():
#     seaborn.lineplot(y=titanic['fare'],x=titanic['age'],data=titanic).set_title('Lmao')
#     plt.show()
# lineChartPlot()
def testCountPlot():
    seaborn.countplot(x=titanic['alive']).set_title('Lmao')
    plt.show()

def testStripPlot():
    seaborn.stripplot(x=titanic['class'],y=titanic['fare'], jitter= True).set_title('ewfwef')
    plt.show() 
testStripPlot()
