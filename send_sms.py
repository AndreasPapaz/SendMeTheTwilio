from twilio.rest import Client

account_sid = 'ACf0d23e492b6558493ecbe708fa8cb292'
auth_token = 'd279750e386d3cc08fe35f658d51644f'
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+12242689098',
         to='+18478776036'
     )

print(message.sid)
