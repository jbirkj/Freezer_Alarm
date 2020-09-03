#
import os
from twilio.rest import Client


#account_sid = 'AC6a93aee8e015bb60e7a0549b43397954'
#auth_token = '80c47500e6343b44b59cabc066c42683'

#sid = os.getenv('TWILIO_ACCOUNT_SID')
#token = os.getenv('TWILIO_AUTH_TOKEN')

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

