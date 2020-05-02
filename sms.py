#pip install twilio  or use Telecoms cloud
from twilio.rest import Client

def send_deposit_notify(b,msg_b):
	account_sid='AC589b2c745015ebef50a451c1fc4dbea0'
	auth_token='75e71828998d121366e64eae4e37f733'
	client=Client(account_sid,auth_token)
	message=client.messages.create(body=msg_b,from_='+12568414997',to=b)
	
def send_credit_notify(a,msg_a):
	account_sid='AC589b2c745015ebef50a451c1fc4dbea0'
	auth_token='75e71828998d121366e64eae4e37f733'
	client=Client(account_sid,auth_token)
	message=client.messages.create(body=msg_a,from_='+12568414997',to=a)

def send_sms_notfy(a,b,amt):
	
	#number='+917683074465'
	msg_b=f'Debited with {amt}Rs'
	msg_a=f'Credited with {amt}Rs'
	b='+91'+str(7683074465)	#change number here 'b'
	a='+91'+str(7683074465) #change number here 'a'
	send_deposit_notify(b,msg_b)
	send_credit_notify(a,msg_a)

def send_sms_otp(otp,number):
	account_sid='AC589b2c745015ebef50a451c1fc4dbea0'
	auth_token='75e71828998d121366e64eae4e37f733'
	number='+91'+str(number)
	client=Client(account_sid,auth_token)
	message=client.messages.create(body='The OTP is '+str(otp),from_='+12568414997',to='+917683074465')#change number here
	print(message.sid)

if(__name__=='__main__'):
	send_sms_notfy()
	send_sms_otp()