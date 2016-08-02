#Questsms Bulk SMS API PYTHON

<h3>Table of contents</h3>

1. Installation 
2. Sending sms
3. Checking Balance 
4. Scheduling sms
5. Marketing Lists
6. Add to marketing list

<h3>Installation</h3>

Quest sms is very easy to use and install. Download or clone  questsms module from the git hub link below.

https://github.com/kikuyu1/quest-api-python

All you need to do now is to include Quest the questsms module in your project like any other normal python module 

<h3>Sending a Simple SMS</h3>

To send sms you need to follow these 3 simple steps
<h4>1. Import SendSms class from questsms module</h4>

From questsms import SendSms
<h4>2. Create an instance of class </h4>
You need to pass 5 arguments

<strong>api_key</strong>

This is your api key.its required and it should not be null
Register an account with <a href="https://questdesigners.com">Quest Web Developers Ltd</a> to get API key at http://account.questdesigners.com

 <pre>Api-key = ‘your api key’ </pre>

<strong>Sender</strong>
This is the name that appears to the  recipients

 <pre>Sender  = ‘your sender id’ </pre>

<strong>Username</strong>
This is your username when your sign up

 <pre> Username = ‘your username’ </pre>

<strong> Message </strong>

This is the message you want to send. 

 <pre>Message = ‘your message’ </pre>

<strong>To </strong>

This should be a recipients phone no. It can be single no or list of numbers.

 <pre>to = ‘+254722....56’ </pre>

Or

 <pre>to = [‘+254722....56’, ‘+254722....45’, ‘+254722....22’] </pre>

Example of SendSms instance is


<pre>sms = SendSms(api_key = ‘your key’, sender=’your sender ID’, 					username=’your username’, message = ‘your message’, 		to=‘+254722....56’)</pre>


<h4>3. The final step is to call the send sms method</h4>

<pre>sms.send()</pre>


<h3>Checking Balance</h3>

To check your sms balance through api you need the following three simple steps

<h4>1. Import CheckBalance class from questsms module	</h4>					
from questsms import CheckBalance

<h4>2. Create an instance of CheckBalance</h4>

You need to pass two arguments 

<strong>Api-key </strong>

<pre>api-key = “your key” </pre>

<strong>Username </strong>

 <pre>username = “your username” </pre>

Example if instance include.

 <pre>c = CheckBalance(api-key=”key” , username= “user”)</pre>

<h4>3. Finally is to call the check() method which return balance as string</h4>


<pre> c = check()</pre>


<h3>SHEDULE SMS</h3>

ScheduleSMS is similar to send sms except it has one additional field 

<pre>sendondate = “shedule date”</pre>

The sendondate on date should contain date in future with the following format <strong>“YYYY-mm-dd H:M:S”</strong>

To send sms you need to follow these 3 simple steps

<h4>1. Import SendSms class from questsms module</h4>

From questsms import SendSms
<h4>2. Create an instance of class </h4>

You need to pass 5 arguments

<strong>Api_key </strong>

This is your api key.its required and it should not be null

 <pre>Api-key = ‘your api key’</pre> 

<strong>Sender</strong>

This is the name that appears to the  recipients

<pre> Sender  = ‘your sender id’ </pre>

<strong> Username </strong>

<pre> Username = = ‘your username’ </pre>

<strong> Message</strong>

This is the message you want to send. 

<pre>Message = ‘your message’</pre>

<strong>To</strong>

This should be a recipients phone no. It can be single no or list of numbers.

<pre>to = ‘+254722....56’</pre>
Or
<pre>to = [‘+254722....56’, ‘+254722....45’, ‘+254722....22’]</pre>

Example of SendSms instance is

<strong>Sendondate</strong>

<pre>Sendondate = “shedule date”</pre>

<pre> sms = SendSms(api_key = ‘your key’, sender=’your sender ID’,	username=’your username’, message = ‘your message’, to=‘+254722....56’, sendondate = “shedule date” )</pre>

<h4> 6. The final step is to call the send sms method</h4>

<pre>sms.schedule()</pre>

<h3> MARKETING LIST</h3>

To check your marketing list through api you need the following three simple steps

<h4>Import MarketingLists class from questsms module</h4>

From questsms import MarketingLists

<h4>Create an instance of CheckBalance</h4>

You need to pass two arguments 

<strong>Api-key</strong>

<pre>api-key = “your key”</pre>

<strong>Username</strong>

<pre>username = “your username”</pre>

Example if instance include.

<pre>m = MarketingLists(api-key=”key” , username= “user”)</pre>

<h4>Finally is to call the get_list() method which return marketing lists</h4>

<pre>m = get_list()</pre>


<h3>Add To Marketing</h3>

To add marketing list through api you need the following three simple steps

<h4>1. Import MarketingLists class from questsms module</h4>	

from questsms import AddToMarketing

<h4>2. Create an instance of AddToMarketing</h4>

You need to pass two arguments 

<strong>Api-key</strong>
<pre>api-key = “your key”</pre>

<strong>Username</strong>
<pre>username = “your username”</pre>



<strong>Name</strong>
<pre>Name = “Subscriber's Name”</pre>

<strong>Phone</strong>
<pre>Phone = “Subscriber's Phone Number (including country code)”</pre>

<strong>List_id</strong>
<pre>List_id = “Desired marketing list ID”</pre>


<pre>m = AddToMarketing(api-key=”key” , username= “user”, 			name=”Subscriber”, phone=”phone”, list_id=”list ID”)</pre>

<h4>3. Finally is to call the get_list() method which return marketing lists</h4>
<pre>m.add_list()</pre>
