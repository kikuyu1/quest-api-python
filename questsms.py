import requests
from datetime import datetime

class SendSms(object):
	"""
	This class is used to send single sms to one person
	"""
	def __init__(self, *args, **kwargs):
		self.url = 'http://account.questdesigners.com/API/?action=compose'
		if 'api_key' in kwargs :
			if kwargs['api_key']:
				self.api_key = kwargs['api_key']
			else:
				raise ValueError('api key cannot be null')
		else:
			raise ValueError('API key must be supplied')


		if 'sender' in kwargs: 
			if kwargs['sender']:
				self.sender = kwargs['sender']
			else:
				raise ValueError('Sender cannot be Null')
		else:
			raise ValueError('Sender not supplied')

		if 'username' in kwargs:
			if kwargs['username']:
				self.username = kwargs['username']
			else: 
				raise ValueError('username cannot be empty')
		else:
			raise ValueError('Username Not supplied')

		if 'to' in kwargs:
			if kwargs['to']:
				self.to = kwargs['to']
			else:
				raise ValueError('reciever cannot be empty')
		else:
			raise ValueError('you must supply the reciever')

		if 'message' in kwargs:
			if kwargs['message']:
				self.message = kwargs['message']
			else:
				raise ValueError('Message cannot Be empty')
		else:
			raise ValueError('You Must Supply Message')
		
	
	def get_url(self):
		return self.full_url

	def send(self):
		if type(self.to) is list:
			for i, val in enumerate(self.to):
				full_url = self.url+'&username='+self.username+'&api_key='+self.api_key+'&sender='+self.sender+'&to='+val+'&message='+self.message
				r = requests.get(full_url)

		if type(self.to) is str:
			full_url = self.url+'&username='+self.username+'&api_key='+self.api_key+'&sender='+self.sender+'&to='+self.to+'&message='+self.message
			r = requests.get(full_url)
			self.status_code = r.content

	def check_status(self):
		return self.status_code


class CheckBalance:
	"""
	This class is used to check balance of available sms
	"""
	def __init__(self, *args, **kwargs):
		self.url = 'http://account.questdesigners.com/API/?action=balance'
		if 'api_key' in kwargs :
			if kwargs['api_key']:
				self.api_key = kwargs['api_key']
			else:
				raise ValueError('api key cannot be null')
		else:
			raise ValueError('API key must be supplied')

		if 'username' in kwargs:
			if kwargs['username']:
				self.username = kwargs['username']
			else: 
				raise ValueError('username cannot be empty')
		else:
			raise ValueError('Username Not supplied')

	def check(self):
		full_url = self.url+'&username='+self.username+'&api_key='+self.api_key
		r = requests.get(full_url)
		print r.content
		return r.content


class ScheduleSMS(SendSms):
	""""""
	def __init__(self, *args, **kwargs):
		super(ScheduleSMS, self).__init__(*args, **kwargs)
		self.url = 'http://account.questdesigners.com/API/?action=schedule'
		if 'sendondate' in kwargs:
			if kwargs['sendondate']:
				time = kwargs['sendondate']
				date_format = "%Y-%m-%d %H:%M:%S"
				now = datetime.now()

				if datetime.strptime(time, date_format) < now:
					print 'date must be in future'
					raise ValueError('date must be in future')
				else:
					self.schedule_time = time 
				
			else:
				raise ValueError('shedule cannot be cannot Be empty')
		else:
			raise ValueError('You Must Supply shedule time')
		
	
	def schedule(self):
		if type(self.to) is list:
			for i, val in enumerate(self.to):
				full_url = self.url+'&username='+self.username+'&api_key='+self.api_key+'&sender='+self.sender+'&to='+val+'&message='+self.message
				r = requests.get(full_url)
				print r.content

		if type(self.to) is str:
			full_url = self.url+'&username='+self.username+'&api_key='+self.api_key+'&sender='+self.sender+'&to='+self.to+'&sendondate='+self.schedule_time+'&message='+self.message
			r = requests.get(full_url)
			print full_url
			self.status_code = r.content
			print r.content

class MarketingLists(object):
	"""docstring for MarketingLists"""
	def __init__(self, *args, **kwargs):
		super(MarketingLists, self).__init__()
		self.url = 'http://account.questdesigners.com/API/?action=marketing_list'
		if 'api_key' in kwargs :
			if kwargs['api_key']:
				self.api_key = kwargs['api_key']
			else:
				raise ValueError('api key cannot be null')
		else:
			raise ValueError('API key must be supplied')

		if 'username' in kwargs:
			if kwargs['username']:
				self.username = kwargs['username']
			else: 
				raise ValueError('username cannot be empty')
		else:
			raise ValueError('Username Not supplied')

		
	def get_list(self):
		full_url = self.url+'&username='+self.username+'&api_key='+self.api_key
		r = requests.get(full_url)
		print full_url
		print r.content
		return r.content


class AddToMarketing(object):
	"""docstring for MarketingLists"""

	def __init__(self, *args, **kwargs):
		super(AddToMarketing, self).__init__()
		self.url = 'http://account.questdesigners.com/API/?action=add_to_list'
		if 'api_key' in kwargs :
			if kwargs['api_key']:
				self.api_key = kwargs['api_key']
			else:
				raise ValueError('api key cannot be null')
		else:
			raise ValueError('API key must be supplied')

		if 'username' in kwargs:
			if kwargs['username']:
				self.username = kwargs['username']
			else: 
				raise ValueError('username cannot be empty')
		else:
			raise ValueError('Username Not supplied')

		if 'name' in kwargs:
			if kwargs['name']:
				self.name = kwargs['name']
			else: 
				raise ValueError('name cannot be empty')
		else:
			raise ValueError('name Not supplied')

		if 'phone' in kwargs:
			if kwargs['phone']:
				self.phone = kwargs['phone']
			else: 
				raise ValueError('phone cannot be empty')
		else:
			raise ValueError('phone Not supplied')

		if 'list_id' in kwargs:
			if kwargs['list_id']:
				self.list_id = kwargs['list_id']
			else: 
				raise ValueError('phone cannot be empty')
		else:
			raise ValueError('phone Not supplied')

		
	def add_list(self):
		full_url = self.url+'&username='+self.username+'&api_key='+self.api_key+'&list_id='+self.list_id+'&name='+self.name+'&phone='+self.phone
		r = requests.get(full_url)
		print full_url
		print r.content
		return r.content