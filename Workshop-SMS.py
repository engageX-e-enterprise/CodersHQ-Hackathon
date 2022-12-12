import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = "AC4677df5a4b92eb6ca8a7705138715e28"
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
PHONE_NUMBNER = os.getenv('PHONE_NUMBNER')



client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body='Hi there',
    from_=PHONE_NUMBNER,
    to='+971508440128'
)

print(message.sid)