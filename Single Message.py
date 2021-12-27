# import schedule
from twilio.rest import Client


# add something to find out who still has / has not paid


def send_message(phone_number='+19544949167'):
    # account_sid = os.environ[sid]
    # auth_token = os.environ[auth_token]
    client = Client('AC0d6981533b67f97c77c927c421d50ae3', '8f4e7dee0668864fdb32b41075ce815d')

    message = client.messages \
        .create(body=f'Psst wanna go now',
                from_='+14155490279',
                to='+18587752732'
                )

    print(message.sid)


send_message()
