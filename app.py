#app.py

import os, sys
import time, datetime

from ds18b20 import read_temp, OneW_init
from Message import send_Whatsappmessage
from TemperatureEventClass import TempEvent
from decouple import config                     #for reading environment variables

deviceFile1, deviceFile2 = OneW_init()
interval = 10

sid = config('TWILIO_ACCOUNT_SID')
token = config('TWILIO_AUTH_TOKEN')


Freezer_1 = TempEvent(30, 'upper', 'Freezer 1')
Freezer_2 = TempEvent(30, 'upper', 'Freezer 2')

while True: 
    try:
        t = datetime.datetime.now()
        
        tCel_1 = read_temp(deviceFile1)
 #       print(str(tCel_1))
        tCel_2 = read_temp(deviceFile2)
 #       print(str(tCel_2))

        #if (Freezer_1.EvalTemperature( read_temp(deviceFile1), t) ):
        if (Freezer_1.EvalTemperature( tCel_1, t) ):
            Freezer_1.Announce(t, sid, token)

        if (Freezer_2.EvalTemperature( tCel_2, t) ):
            Freezer_2.Announce(t, sid, token)

        #time.sleep(300)
        for i in range(1, interval):      #prevent system hang by waiting range(30) seconds
            time.sleep(1)


    except KeyboardInterrupt:
        print("Program interrupted by Keyboard!")
        break

print("Goodbye")