# SMS functions file
import main


# function to send SMS messages from an account to others
def send_sms_message(message,from_user,to_user):

    message = main.client.messages \
                    .create(
                         body=message,
                         from_=from_user,
                         to=to_user
                     )

    print(message.sid)