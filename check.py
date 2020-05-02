#import getpass
#import stdiomask
import re
import random
from sms import *
from tkinter import *
from tkinter import ttk

def check_pass(p):
	#p=stdiomask.getpass(mask='*')
	'''p=getpass.getpass("Enter your password: ",'*')
	print(p)'''
	#if re.match(r'[A-Z]+[a-z0-9]+[@#$%^&+=]{8,}', p):
	if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', p):
		return True
	else:
		return False

def check_email(s):
	if(re.match("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$",s)!=None):
		return True
	else:
		return False

def check_otp(number):
	
	otp=random.randint(0000,9999)
	send_sms_otp(otp,number)
	return otp
	
	
	
def check_number(phone):
	try:
		phone_number=int(phone)
	except ValueError:
		return False
	if(re.match("[7-9][0-9]{9}",str(phone_number))!=None):
		return phone_number
	else:
		return False
	
		
		
if(__name__=='__main__'):
	#print(check_email('monu@gmail.com'))
	#print(check_pass())
	print(check_number(2151))