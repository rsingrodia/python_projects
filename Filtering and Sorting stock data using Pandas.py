import pandas as pd
import matplotlib.pyplot as plt

fb = pd.read_csv('FB.csv')
goog = pd.read_csv('GOOG.csv')
tsla = pd.read_csv('TSLA.csv')

st_date = str(fb.iloc[0,0])
en_date = str(fb.iloc[len(fb.index)-1,0])

keepgoing = 'y'
beg_date = input('Enter the beginning date between {} and {}: '.format(st_date,en_date))

while keepgoing == 'y':
    if pd.to_datetime(st_date) <= pd.to_datetime(beg_date) <= pd.to_datetime(en_date):
        keepgoing = 'n'
    else:
        print('Start date is out of the date range')
        keepgoing = 'y'        
        beg_date = input('Enter the beginning date between {} and {}: '.format(st_date,en_date))
        
going = 'y'        
end_date = input('Enter the ending date between {} and {}: '.format(st_date,en_date))

while going == 'y':
    if pd.to_datetime(beg_date) <= pd.to_datetime(end_date) <= pd.to_datetime(en_date):
        going = 'n'
    elif pd.to_datetime(st_date) <= pd.to_datetime(end_date) <= pd.to_datetime(en_date):
        print('End date cannot be before start date')
        going = 'y'        
        end_date = input('Enter the beginning date between {} and {}: '.format(st_date,en_date))
    else:
        print('End date is out of date range')
        going = 'y'        
        end_date = input('Enter the beginning date between {} and {}: '.format(st_date,en_date))


fb_new = fb[(fb['Date']>=beg_date) & (fb['Date']<=end_date)]
goog_new = goog[(goog['Date']>=beg_date) & (goog['Date']<=end_date)]
tsla_new = tsla[(tsla['Date']>=beg_date) & (tsla['Date']<=end_date)]

beg_fb = fb_new.iloc[0,1]
beg_goog = goog_new.iloc[0,1]
beg_tsla = tsla_new.iloc[0,1]

end_fb = fb_new.iloc[len(fb_new.index)-1,4]
end_goog = goog_new.iloc[len(fb_new.index)-1,4]
end_tsla = tsla_new.iloc[len(fb_new.index)-1,4]

min_fb = fb_new['Low'].min()
min_goog = goog_new['Low'].min()
min_tsla = tsla_new['Low'].min()

max_fb = fb_new['High'].max()
max_goog = goog_new['High'].max()
max_tsla = tsla_new['High'].max()

avg_fb = fb_new['Adj Close'].mean()
avg_goog = goog_new['Adj Close'].mean()
avg_tsla = tsla_new['Adj Close'].mean()

print('\n\nSummary of stock prices from', beg_date, 'to', end_date)

print('\n{}\t{:>10}\t{:>15}\t{:>10}\t{:>8}\t{:>8}'.format('','Beginning Price', 'Ending Price', 'Minimum', 'Maximum', 'Average'))
print('Symbol')
print(('{}\t{:15,.2f}\t{:15,.2f}\t{:10,.2f}\t{:8,.2f}\t{:8,.2f}'.format('FB',beg_fb,end_fb,min_fb,max_fb,avg_fb)))
print(('{}\t{:15,.2f}\t{:15,.2f}\t{:10,.2f}\t{:8,.2f}\t{:8,.2f}'.format('GOOG',beg_goog,end_goog,min_goog,max_goog,avg_goog)))
print(('{}\t{:15,.2f}\t{:15,.2f}\t{:10,.2f}\t{:8,.2f}\t{:8,.2f}'.format('TSLA',beg_tsla,end_tsla,min_tsla,max_tsla,avg_tsla)))

fb_new['Symbol']=('FB')
goog_new['Symbol']=('GOOG')
tsla_new['Symbol']=('TSLA')

pd.options.mode.chained_assignment = None
final = pd.concat([tsla_new,fb_new,goog_new])

final.pivot(index='Date', columns='Symbol', values='Adj Close').plot()

plt.xlabel("Date")
plt.xticks(rotation=60)
plt.ylabel("Price ($)")
plt.title("Stock Prices")
plt.grid(False)


