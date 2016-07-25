from questsms import SendSms
api_key = 'yourapikey'
sms = SendSms(api_key=api_key, sender='Quest-web', username='yourusername', message='your message', to=['+2547******', '+2547******'])

sms.send()
