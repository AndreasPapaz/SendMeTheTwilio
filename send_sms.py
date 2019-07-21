import cred
from twilio.rest import Client

account_sid = cred.account_sid
auth_token = cred.auth_token
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12242689098',
         to='+18478776036'
     )

print(message.sid)
