from questsms import ScheduleSMS

api_key = '3fc1e09e231e517688410ab8256a8402:EFs6G8wAeriygvaRvalj8XkjR8W87DvC'
sms = ScheduleSMS(api_key=api_key, sendondate='2017-07-23 4:30:00', sender='Quest-web', username='nderitupatrick4', message='fracis sheduled', to='+254729930509')
sms.schedule()