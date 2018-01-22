import pandas as pd
import quandl

df= quandl.get('WIKI/GOOGL')
df= df[['Adj. Open','Adj. Close','Adj. Low','Adj. High', 'Adj. Volume']]

df['HL_PCT']= (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100
df['percent_change'] = (df['Adj. Close']- df['Adj. Open'])/df['Adj. Open']*100
df= df[['Adj. Close', 'HL_PCT', 'percent_change', 'Adj. Volume', 'Adj. Open']]

print('this is the answer')

print(df.head()) #this prints all the column of the data provided to us

