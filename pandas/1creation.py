#here is  how to create a data frame in pandas

#1. array - we can create data frame by 2d array of numpy np.array=([1,2],[3,4])
#2.dictonary - a dict contain key value pair where a column ahould be your feature and data should be your list so you can store multiple data
#3 use list 
#csv file-

import pandas  as pd
import numpy as np

#creation of data frame by array

c = np.array([[1,2],[3,4],[4,5]])

df = pd.DataFrame(c,index=['row1','row2','row3'],columns=['col1','col2']) #data frame is a function use to show data in framing manner
print(df)


# creation of data frame using list
c = [[1,2],[3,4],[4,5]]

df = pd.DataFrame(c,index=['row1','row2','row3'],columns=['col1','col2']) #data frame is a function use to show data in framing manner
print(df)
#creation of data frame using dic

marks=[32,34,13,52,52,16,78,5]
name=["p","o",'y','t','r','r','e','w']
dic={
    "name":name,
    "marks":marks
}

print(pd.DataFrame(dic))

#creation of dat frame by csv file
df = pd.read_csv("/home/punit/Documents/Ds/pandas/StudentsPerformance.csv")
#here the all csv filw will display but as we want some datas daya frame
df=pd.DataFrame(df)
print(df)




