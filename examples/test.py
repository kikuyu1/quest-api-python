from questsms import SendSms
api_key = '3fc1e09e231e517688410ab8256a8402:EFs6G8wAeriygvaRvalj8XkjR8W87DvC'
sms = SendSms(api_key=api_key, sender='Quest-web', username='nderitupatrick4', message='hi everyone', to=['+254729930509', '+254702681502'])

sms.send()