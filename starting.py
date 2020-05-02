from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from start_program import *
from customer import *
from check import *
from admin_page import *
import create_base_tables as cbt
#from tkinter.ttk import *

#*******************************functionalite************************************

def Login_page(loger_type,acc_enrty,password_entry,root):
	type=loger_type.get()
	acc=acc_enrty.get()
	pass_word=password_entry.get()
	if(acc==''or pass_word==''):
		mb.showinfo('Info','Please fillup all the options')
	else:
		try:
			acc=int(acc)
		except Exception:
			mb.showerror('Error','Account should be integer')
		else:
			if(type=='Admin'):
				try:	
					import start_program as sp
					ans=sp.admin_login(acc,pass_word)		#show error admin_login not define
					if(ans[0]!=False):
						root.destroy()
						admin_access(ans[1])
				except Exception:
					mb.showerror('Error','Id or password not correct')
				
			else:
				try:
					'''import start_program as sp
					a=sp.login(acc,pass_word)		# show error when we want login again.
					if(True==a[1]):
						root.destroy()
						customer(a[0][0])'''
					import start_program as sp
					a=sp.login(acc,pass_word)		# show error when we want login again.
					if(True==a[1]):
						root.destroy()
						import customer as c
						c.customer(a[0][0])
					
				except Exception as e:
					print(e)
					mb.showerror('Error','Id or password not correct'+str(e))
				
				
def sumit_detail(entry_list,cus_var):
	
	detail_list=['Name','f_name','gender','yy','mm','dd','address','phone','email','password']
	count=0
	for i in entry_list:
		detail_list[count]=entry_list[i].get()
		count+=1
	if('' in detail_list):
		mb.showerror('Error','fill the all requirement')
	else:
		
		ans=check_number(detail_list[7])
		if(ans==False):
			mb.showerror('Error','Phone number should be integer and 10 digits')
		else:
			if(check_email(detail_list[8])==True):
				if(check_pass(detail_list[9])==True):
					import start_program as sp
					sp.new_user(detail_list)
					#mb.showinfo('info','your account successfully created')
				else:
					mb.showerror('Error','In Password should be include symbol,digits and characters Ex:-monu@123')
			else:
				mb.showerror('error','Enter valid email id')
		cus_var.delete(len(cus_var))	

def forget_pass(ac):
	root1=Tk()
	root1.title('Froget password')
	
	def fun4(new_password,old_fra,ac):
		old_fra.destroy()
		root1.destroy()
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		
		cursor.execute(f"update account set password='{new_password}' where ac_no={ac}")
		mb.showinfo('info','Password successfully changed')
		con.commit()
		con.close()
	
	def fun3(otp,ent_otp,old_frame,ac):
		old_frame.destroy()
		frame3=ttk.Frame(root1)
		
		if(otp!=ent_otp):
			lab3=ttk.Label(frame3,text='Set new password:-',font=('',15,'bold'))
			lab3.grid(row=0,column=0,padx=5,pady=5)
			
			entry_var3=StringVar()
			entry3=ttk.Entry(frame3,width=15,textvariable=entry_var3)
			entry3.grid(row=0,column=1,padx=5,pady=5)
			
			btn3=ttk.Button(frame3,text='Sumit',command=lambda:fun4(entry3.get(),frame3,ac))
			btn3.grid(row=1,columnspan=1,padx=5,pady=10)
			
		else:
			mb.showerror('Error','Otp not match')
			
		frame3.pack()
	
			
	
	def fun2(old_frm,phone,ac):
		old_frm.destroy()
		frame2=ttk.Frame(root1)
		print(ac,'fun2')
		otp=check_otp(phone)
		print(otp)
		lab2=ttk.Label(frame2,text='Enter the otp:-',font=('',15,'bold'))
		lab2.grid(row=0,column=0,padx=5,pady=5)
		
		entry_var2=StringVar()
		entry2=ttk.Entry(frame2,width=15,textvariable=entry_var2)
		entry2.grid(row=0,column=1,padx=5,pady=5)
		
		btn2=ttk.Button(frame2,text='Sumit',command=lambda:fun3(otp,entry2.get(),frame2,ac))
		btn2.grid(row=1,columnspan=1,padx=5,pady=10)
		
		frame2.pack()
	
	
	
	frame1=ttk.Frame(root1)
	lab1=ttk.Label(frame1,text='Enter the Phone no:-',font=('',15,'bold'))
	lab1.grid(row=0,column=0,padx=5,pady=5)
	
	entry_var=StringVar()
	entry1=ttk.Entry(frame1,width=20,textvariable=entry_var)
	entry1.grid(row=0,column=1,padx=5,pady=5)
	
	btn=ttk.Button(frame1,text='Sumit',command=lambda:fun2(frame1,entry1.get(),ac))
	btn.grid(row=1,columnspa=1,padx=5,pady=10)
	
	frame1.pack()
	root1.geometry('400x150+350+250')
	root1.mainloop()
	
	
	
	
				
def exit(root):
	root.destroy()

#******************************************Functionality End**************************************

#********************************************Starting Program**************************************
def start():
	
	root=Tk()
	root.title('Simple Banking Management System')
	title_lable=Label(root,text='SIMPLE BANKING MANAGEMENT SYSTEM',font=('Bahnschrift SemiBold',35),bg='Blue',fg='White')
	title_lable.pack()

	nb=ttk.Notebook(root)
	page1=Frame(nb)
	page2=ttk.LabelFrame(nb,text='Create @ Account')
	page3=ttk.LabelFrame(nb,text='About US')

	nb.add(page1,text='Login')
	nb.add(page2,text='sing up')
	nb.add(page3,text='About Us')

	nb.pack(expand=True,fill='both')

	#*******************************Login page1***************************************
	
	loger_lable=ttk.Label(page1,text='Loger Type:-')
	loger_lable.grid(row=1,column=0,padx=5,pady=5,sticky='w')
	
	loger_type=StringVar()

	loger=ttk.Combobox(page1,width=17,textvariable=loger_type,state='readonly')
	loger['value']=('customer','Admin')												#commbo button
	loger.current(0)
	loger.grid(row=1,column=1,sticky='w',padx=5,pady=5)

	Account_no=ttk.Label(page1,text='Account No:-')
	Account_no.grid(row=2,column=0,padx=5,pady=5)

	password=ttk.Label(page1,text='Password:-')
	password.grid(row=3,column=0)

	acc_var=StringVar()

	acc_enrty=ttk.Entry(page1,width=20,textvariable=acc_var)
	acc_enrty.grid(row=2,column=1,padx=5,pady=5)
	acc_enrty.focus()

	pass_var=StringVar()

	password_entry=ttk.Entry(page1,width=20,textvariable=pass_var,show='*')
	password_entry.grid(row=3,column=1,padx=5,pady=5)

	sumitbtn=ttk.Button(page1,text='Login',command=lambda: Login_page(loger_type,acc_enrty,password_entry,root))
	sumitbtn.grid(row=4,columnspan=2,pady=6)
	
	
	forget_password_btn=ttk.Button(page1,text='Forget Password',command=lambda: forget_pass(acc_enrty.get()))
	forget_password_btn.grid(row=4,column=3)

	exitbtn=ttk.Button(page1,text='Exit',command=lambda:exit(root))
	exitbtn.place(x=130,y=150)


	#********************************************singup page2**********************************************

	list1=['Name:-',"Father's Name:-",'Gender:-','D.O.B(yy/mm/dd):-','Address:-','Phone no.:-','Email-Id','Password']
	 
	for i in range(len(list1)):
		cust_var='variable'+ str(i)
		cust_var=ttk.Label(page2,text=list1[i])
		cust_var.grid(row=i,column=0,sticky='w',padx=5,pady=5)

	entry_list={
	'name':StringVar(),
	'f_name':StringVar(),
	'gender':StringVar(),
	'yy':StringVar(),
	'mm':StringVar(),
	'dd':StringVar(),
	'address':StringVar(),
	'phone_no':StringVar(),
	'email_id':StringVar(),
	'password':StringVar()
	}

	count=0
	for i in entry_list:
		cus_var='entry'+ i
		if(count!=2 and count!=3 and count!=4 and count!=5 ):
			if(count!=9):
				cus_var=ttk.Entry(page2,width=20,textvariable=entry_list[i])
			else:
				cus_var=ttk.Entry(page2,width=20,textvariable=entry_list[i],show='*')
		else:
			
			cus_var=ttk.Combobox(page2,width=10,textvariable=entry_list[i],state='readonly')
			if(count==2):
				cus_var['value']=('Male','Female','Others')
				cus_var.current(0)
			elif(count==3):
				cus_var['value']=(1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007)
				cus_var.current(7)
			elif(count==4):
				cus_var['value']=(1,2,3,4,5,6,7,8,9,10,11,12)
				cus_var.current(0)
				cus_var.grid(row=count-1,column=2,sticky='w',padx=5,pady=5)
			else:
				cus_var['value']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
				cus_var.current(0)
				cus_var.grid(row=count-2,column=3,sticky='w',padx=5,pady=5)
			
				
		if(count>5 or count<4):
			if(count==3):
				cus_var.grid(row=count,column=1,sticky='e',padx=5,pady=5)
			else:
				if(count>=6):
					cus_var.grid(row=count-2,column=1,sticky='W',padx=5,pady=5)
				else:
					cus_var.grid(row=count,column=1,sticky='W',padx=5,pady=5)
		count+=1

	sumit_btn=ttk.Button(page2,text='Sumit',command=lambda:sumit_detail(entry_list,cus_var))
	sumit_btn.grid(row=count,columnspan=2,pady=5)
	

	#********************************************About us page3*******************************

	text_page=Text(page3)
	text_page.config(wrap='word',relief=FLAT)

	scroll_bar=Scrollbar(page3)
	scroll_bar.pack(side='right',fill='y')

	text_page.focus_set()
	text_page.pack(fill='both',expand=True)

	scroll_bar.config(command=text_page.yview)
	text_page.config(yscrollcommand=scroll_bar.set)
	
	text_page.insert(END,f'Simple Banking Management System \n \n \t This Porject is made by Monu sharma and Pankaj Jaswal(B.tech-CSE-3rd yr-5th sem)\n and security advisor udit sharma','Big')
	text_page.insert(END,'\n---------------------------------------------------------------------------------------------------','Big')
	text_page.insert(END,'\n\t\tThis poject is made using Python and Mysql \n\n\n \t\t Thanks for using this program:)','Big')

	root.geometry('900x550+250+100')
	root.mainloop()

if(__name__=='__main__'):
	cbt.create_main_tables()
	start()
	