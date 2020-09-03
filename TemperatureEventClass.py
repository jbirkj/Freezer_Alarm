#TemperatureEventClass.py
from datetime import timedelta, datetime
from Message import send_Whatsappmessage

class TempEvent():

    def __init__(self, l, c, n):
        self.t_eventstart = 0
        self.limit = l
        self.condition = c
        self.messagecount = 0
        self.name = n

    def __repr__(self):
        return str(self.messagecount)+' '+ str(self.t_eventstart)


    def EvalTemperature(self, temperature, time_):
        #evaluate temperature 
        if (temperature == 99999):
            return 0
        elif (self.condition == 'upper'):
            if ( temperature > self.limit):
                if (self.t_eventstart == 0):
                    self.t_eventstart = time_
                    self.messagecount = 1
#                    print('event start: '+str(time_))
                return 1
            else:
                self.messagecount = 0
                return 0
        elif ( self.condition == 'lower'):
            if ( self.temperature < self.limit):
                if (self.t_eventstart == 0):
                    self.t_eventstart = time_
                    self.messagecount = 1
                return 1
            else:
                self.messagecount = 0
                return 0
        else:
            self.t_eventstart = 0
            self.messagecount = 0
            return 0

    def Announce(self, t, sid, token):

#        if (t > self.t_eventstart + timedelta(seconds=60) ):        #wait 60seconds before first announcement

        if ( t > (self.t_eventstart + timedelta(seconds=(60*self.messagecount)))):
            print('Message '+ str(self.messagecount) + ' at ' + str(self.t_eventstart))
            send_Whatsappmessage('Temperature is ' + 
                                    self.condition + 
                                    'than ' + 
                                    str(self.limit) + 
                                    'for ' + 
                                    str(self.messagecount) + 
                                    'minutes now in ' +
                                    self.name, sid, token)
            self.messagecount = self.messagecount + 1
#            print('Temperature is ' + 
#                                    self.condition + 
#                                    'than ' + 
#                                    str(self.limit) + 
#                                    'for ' + 
#                                    str(self.messagecount+1) + 
#                                    'minutes now in ' +
#                                    self.name)
                






