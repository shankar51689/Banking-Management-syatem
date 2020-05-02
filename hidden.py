def hide(check):
	c=0
	ready=''
	for i in str(check):
		c+=1
		if(c<=2):
			ready=ready+i
	ready=ready+'x'.center(len(str(check))-2,'x')
	return ready

if(__name__=='__main__'):
	print(hide(125356))
		