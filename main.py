# Main python file
import os
import SMS
import voice
from twilio.rest import Client


#GLOBAL TWILIO INFO:
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['*****'] # twilio account SID
auth_token = os.environ['******'] # twilio auth token
client = Client(account_sid, auth_token)