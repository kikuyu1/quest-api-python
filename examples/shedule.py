from questsms import ScheduleSMS

api_key = 'yourapikey'
sms = ScheduleSMS(api_key=api_key, sendondate='2017-07-23 4:30:00', sender='Quest-web', username='yourusername', message='your scheduled message', to='+25472*****')
sms.schedule()
