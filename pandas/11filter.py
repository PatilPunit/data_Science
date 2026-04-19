#filtering is nothing but the conditing of data as we just et wanted data
# we are using laptop_price.csv for this

import pandas as pd
import numpy as np
# 1.Filter a dat frame based on 1 condition
link = "/home/punit/Documents/Ds/pandas/StudentsPerformance.csv"
link = "/home/punit/Documents/Ds/pandas/laptop_price.csv"
df = pd.read_csv(link,encoding="ISO-8859-1")  #For the unicoding for file in case if  it has some characters doesnt belong to unicode 8

print(df['Company']=='Apple') #use to verify that company has apple name if yes the true otherwise False

print(df[df['Company']=='Apple']) # use to filer comapany based on Apple same with 
print(df[df['TypeName']=='Ultrabook'])

#ok stilkl there is a  big chance that can be other comapanies can came in this filering in case of big data so we will use 

print(df[df['Company']=='Apple'].value_counts('Company')) #we can see a number of only comapnies with apple name

print(df[df['Company']!= 'HP']) # to not show company where HP
print(df['Company']!='HP')

price = 2000
print(df[df['Price_euros'] > price]) # to find laptop over 2000


#create a column based on one condition usinh np.where()

print(df['Price_euros']> price)
print(np.where(df['Price_euros']>price,'Expensive','Cheap'))

df['Price_tag'] = np.where (df['Price_euros']>price,'Expensive','Cheap')
print(df)
print(df.value_counts('Price_tag'))

print(np.where(df['Inches'] < 15,"Big_screen","Small_screen"))
df['Screen']= np.where(df['Inches'] < 15,"Big_screen","Small_screen")
print(df)
print(df.value_counts('Screen'))

#filtering data frame based on multiple condition using & or |

print(df[(df['Company']=='Apple') & (df['Price_euros']> 2000)])

print(df[(df['Company']=='Apple') | (df['Company']=='Dell')])
print(df[((df['Company']=='Apple') | (df['Company']=='Dell')) & (df['Price_euros']> 2000)])


# creating condial column with more than 2 choices using np.select()
# this function takes two arguments as list an return an arrat

conditions=[
    df["Price_euros"] > 3000,
    (df["Price_euros"] >2000)&(df["Price_euros"] < 3000),
    (df["Price_euros"] >800)&(df["Price_euros"] < 2000),
    df["Price_euros"] <800,
]
values =['too Expensive','Expensive','Affordable','Cheap']

df['Price_tier']=np.select(condlist=conditions,choicelist=values,default=' ') # if any kind of error got of dtype diffrent data type the use default = ' '
print(df['Price_tier'])
print(df['Price_tier'].value_counts())


# isin() method fro single connditon

print(df['Company'].isin(['Apple','HP']))
print(df[df['Company'].isin(['Apple','HP'])])

#isin()  for multiple filters
print('\n', '='*70)
f1 =df['TypeName'].isin(['Ultrabook','Notebook'])
f2 = df['Company'].isin(['Apple','HP'])

print(f1 & f2)
print(df[f1 & f2])
df['Filter']=f1 & f2
print(df['Filter'].value_counts())

print('\n', '='*180)


print('\n', '='*180)
#find  duplicated values using df.duplicated
print(df.duplicated('laptop_ID'))
print(df.duplicated('Company').value_counts())
print(df[df.duplicated('Company')])
print(df)

# duplicates in 2 0r more columns
print(df.duplicated(['Product','Inches','Cpu']))
print(df[df.duplicated(['Product','Inches','Cpu'])])
df['duplicate']=df.duplicated(['Product','Inches','Cpu'])
df_dup=df[df['duplicate']].sort_values(['Product','Inches'])
print(df_dup)
print('\n', '='*180)
#to shiw noot dupllicants
print(~df['duplicate'])
unique= df[~df['duplicate']]
print(unique['duplicate'].value_counts())

#droping duplicates usimg drop_duplicate methid 
#below function will give you all the drop the all duplicates in company column
print(df.drop_duplicates(['Company']))
print(df.drop_duplicates(['Company']) [['Company','Price_euros']])

# 3 now finding the cheapest and most expensive laptop per compay
# first sort the dataframe

print(df.sort_values(['Company','Price_euros']))
print(df.drop_duplicates(['Company'],keep='first') [['Company','Price_euros']])
print(df.drop_duplicates(['Company'],keep='last') [['Company','Price_euros']])

# 3 to start the index from 0 by igniring actual index we use
ing_ind=df.drop_duplicates(['Company'],keep='first',ignore_index=True) [['Company','Price_euros']]
print(ing_ind)

sort_screen=df.sort_values(['Company','Inches'])
print(sort_screen)

sm_screen = df.drop_duplicates(['Company'],keep='first',ignore_index=False) [['Company','Inches']]
bg_screen = df.drop_duplicates(['Company'],keep='last',ignore_index=False) [['Company','Inches']]
print(sm_screen)
print(bg_screen)

#unique() - this method provide an array of unique value if series

print(df['Company'].unique())
print(df['Inches'].unique())
print(len(df['Price_euros'].unique()))

print(df['Company'].nunique())