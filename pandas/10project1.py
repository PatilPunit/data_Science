#web scraping - it is process use to extact massive data form website by requestind from python script
import pandas as pd
import numpy  as np
import matplotlib.pyplot as mp
target = "https://www.football-data.co.uk"

# ok so the given link is of the website we are trying to extract data .
# so in this website there are many records or data about the results of football league .
#if we want that data we need to download all files manually but with pandas w can acutomate them .

#readind one csv file  form website
df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2526/E0.csv")
df.rename(inplace=True,columns={"FTHG":"FULL H","FTAG":"FULL A","HTHG ":"HALF H","HTAG":"HALF A"})
print(df)

print(df.dropna(inplace=True))


#multiple links at a time

link = "https://www.football-data.co.uk/mmz4281/" + "2526" + "/"+"E0"+".csv"
dfq=pd.read_csv(link)
print(dfq)

event = ['E0','E1','E2','E3','EC']
frame = []

for i in event:
    dfq=pd.read_csv("https://www.football-data.co.uk/mmz4281/" + "2526" + "/"+i+".csv")
    frame.append(dfq)
print(len(frame))

print(frame)

# multiple seasoms of diffrent years
event = ['E0','E1','E2','E3','EC']
frame = []



for i in event:
    for j in range(15,20) :
      
      dfq =pd.read_csv("https://www.football-data.co.uk/mmz4281/" +  str(j)+str(j+1)+ "/"+i+".csv" ,encoding="unicode_escape")
      frame.append(dfq)

print(frame)



df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2526/E0.csv")
df.rename(inplace=True,columns={"FTHG":"FULL H","FTAG":"FULL A","HTHG ":"HALF H","HTAG":"HALF A"})
print(df.head())
print(df.info())
print(df.describe())

#both of functions are returning none value cause this functions only  modiefies csv file
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

max_golas= list(zip(df["HomeTeam"],df["FULL H"]))

print(np.array(max_golas))
print(dict(max_golas))
print(set(max_golas))


print("                                                                     ")
team=df.groupby('HomeTeam')
df['FULL H'].sum()

for i in team.head():
    print(i)


