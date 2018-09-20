from oligo import iber
import datetime


watt = iber.watthourmeter("mvizcay@gmail.com","2Dejulio")
print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+' '+str(watt))

watt2 = iber.icpstatus("mvizcay@gmail.com","2Dejulio")
print(watt2)