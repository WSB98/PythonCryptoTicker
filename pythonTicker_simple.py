#24/7 crypto ticker in less than 50 lines of code
#imports
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import time
#establish the cryptos you want to track here -> use this website to find the API name, (https://www.coingecko.com/en/api/documentation)
tokenTickers= ['bitcoin','ethereum','cardano','internet-computer','dogecoin']
cg = CoinGeckoAPI() #open API
def updateTime(now): #update time and print string
    #format time
    now = now.split(' ')
    nowString = now[1]
    nowString = nowString.split(':')
    #assign time
    hour = nowString[0]
    minute = nowString[1]
    second = nowString[2]
    #printable string
    string = '\tThe time is: ' + hour+' : '+minute+' : '+second + ', tokens below \n'
    return string
def trimAndPrintPrice(price,tokenName): #format and trim price and token name -> convert to printable string
    string = f'''\t\t\tName: {tokenName}\n\t\t\tPrice: ${str("{:,}".format(price[tokenName]["usd"]))}
    \n\t\t\tMarket Cap: ${str("{:,}".format(price[tokenName]["usd_market_cap"]))}'''
    return string
def customCall(tokenName): #custom token call
    call = cg.get_price(ids=tokenName, vs_currencies='usd', include_market_cap='true') #custom call
    string = trimAndPrintPrice(call,tokenName) #custom trim
    return string
while True: #alert looop
    #iteration and bullet points
    tick,bullets = 0,['o','O']
    #title
    print('\n==================C==R===Y==P==T==O=====T==I==C==K==E==R================== \n')
    time.sleep(2)
    #loading up, waiting, stalling for API
    print('ticking...\n')
    time.sleep(4)
    #show the current time
    print(updateTime(str(datetime.now())))
    time.sleep(3)
    for x in tokenTickers: #loop through all tickers and call each in the API
        if tick % 2 == 0:
            print(f'{bullets[0]}'+'\n'+customCall(x)+'\n')
        else:
            print(f'{bullets[1]}'+'\n'+customCall(x)+'\n')
        time.sleep(2)
        tick+=1
    print('waiting...\n')
    '''print('==================C==R===Y==P==T==O=====T==I==C==K==E==R================== \n\n')'''
    time.sleep(7)