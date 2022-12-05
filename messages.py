# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
account_sid = 'AC5e018ded21db2740ca929b28c0845b49'
auth_token = '757ae8aa5067aa477a9f0318ca8fce32'
client = Client(account_sid, auth_token)

message = client.messages.create(
  body='Hi there',
  from_='+12345423512',
  media_url='https://pbs.twimg.com/media/Faw_-nUWYAEeqRk.jpg',
  to='+15812309887'
)

print(message.sid)