from twilio.rest import Client
import os

# SMS Message
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = 'AC732c080fb503f9922b1dbf7f8e2f7184'
TWILIO_AUTH_TOKEN = '9c277b72619aaf437e356cc8cbd27f2c'
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = TWILIO_ACCOUNT_SID
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

remetente = '+18104258480'
destino = '+5531975128744'

# for item in destino:
message = client.messages \
              .create(
                  body="Olá Guto Senna!",
                  from_=remetente,
                  to=destino
              )
print(message.sid)