# Voice functions file
import main


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# function to send SMS messages from an account to others
def send_voice_message(url,from_user,to_user):
    call = main.client.calls.create(
                            url=url,
                            to=to_user,
                            from_=from_user
                        )

    print(call.sid)