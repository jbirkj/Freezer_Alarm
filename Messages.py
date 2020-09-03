# copy from earlier without ID's
import os
from twilio.rest import Client


def send_Whatsappmessage(message, sid, token):
    client = Client(sid, token)

    message = client.messages.create(
                              body=message,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+4530383133'
                          )
#    message = client.messages.create(
#                              body=message,
#                              from_='+16198666670',
#                              to='+4530383133'
#                          )

#    print(message.sid)

