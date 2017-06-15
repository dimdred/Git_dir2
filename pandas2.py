import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('161003sprd.csv', names=['time_stamp', 'fftt', 'sspot', 'ssprt'], skiprows=1)


print df.head()

#add property of col
#df.new_col = 0
#print df.head()
#print df.__dict__

#add new col
#df['new_col'] = 0
#print df.head()

#update new col
#df.new_col = 1
#print df.head()

#df[start:stop:step]
print df[1:4:2]
#print df[:10000:-1]

print df[3:6]['sspot']
print df[3:6].sspot

print df.loc[:'2016-10-03 10:00:00.837']

print df.loc[:'2016-10-03 10:00:00.837',['sspot', 'ssprt']]

print df[df.sspot >= 62830]
#print df.sspot[lambda s: s > 0]

#task
df['mean_val'] = df.ssprt.mean()
df['min'] = df.ssprt.mean() - df.ssprt.std() #1067.49
df['max'] = df.ssprt.mean() + df.ssprt.std() #1104.59
#df['low'] = [df.sspot - df.min]
print df.head()

print df[df.ssprt == df.ssprt.min()] #986.0
print df[df.ssprt == df.ssprt.max()] #1160.5
#print df.loc['2016-10-03 10:00:00.820':'2016-10-03 10:00:00.860', ['ssprt']]
max_p = df[df.ssprt >= df.ssprt.mean() + df.ssprt.std()]
min_p = df[df.ssprt <= df.ssprt.mean() - df.ssprt.std()]

print max_p.count() #38513
print min_p.count() #17630
print df.count() #208918
#t1 = pd.merge(max_p, min_p, on='mean_val')
#print t1.count() #208918

df.set_index(['ssprt'])
#print df.loc[:1067].sp
print '-------------------------------------------'


#print df.where(df.ssprt >= 1159, 10) #replcae without modification

#print df[df.ssprt >= 1159] = 10 #with modification
#df.query()

r = df.rolling(window=60)
gr = df.groupby(['ssprt'])
print gr.count()
print '-----------------------------------------------'

#df.between(df.ssprt.min(),df.ssprt.mean())
#print df.loc[:].spr.ssprt[:990]

df1 = df[(df.ssprt < (df.ssprt.mean() - df.ssprt.std())) | (df.ssprt > (df.ssprt.mean() + df.ssprt.std()))]

print df1.count()

l = df1.ssprt<(df.ssprt.mean() - df.ssprt.std())
#print l.head()
#l=df1.ssprt<df.min
#print l.unique()
#df1['res']=l
#df1.head()

#task 2 moving average
df2 = df
df2['move_val'] = pd.rolling_mean(df2.ssprt, 1000)
print df2.nunique()
r = df2.rolling(window=60)
df2.ssprt.plot()

plt.figure()

