from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from pymysql import *
import hidden
import sms
from check import *
from starting import *
from modules import *

def logout(root):
	root.destroy()
	start()
	
	
	
def withdraw_fun(amt,root,acc_no):
	try:
		amt=float(amt)
	except ValueError:
		mb.showerror('Error','Enter amount should be in integer or floating point manner')
	else:
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		cursor.execute(f'select * from account where ac_no={acc_no} and T_balance>={amt}')
		if(cursor.rowcount!=0):
			cursor.execute(f'update account set T_balance=T_balance-{amt} where ac_no={acc_no}')
			
			cursor.execute(f'select ac_no,Name,T_balance from account where ac_no={acc_no}')
			c=cursor.fetchall()
			
			update_trans_withdraw(c[0],amt)
			
			mb.showinfo('Info',f'Amount will be successfully withdrawed \n A/c:-{hidden.hide(c[0][0])}\n Name:-{c[0][1]}\n withdrawed amt:-{amt}\n T.amount:-{c[0][2]}')
			#root.destroy()
			
			con.commit()
			con.close()
		else:
			mb.showerror('Error','You have in sufficent balance in your account')
	root.destroy()

	
def withdraw_amt(acc_no):
	 
	root=Tk()
	root.title('Withdraw')
	
	amt_label=ttk.Label(root,text='Enter the withdraw amount:-',font=('',15,'bold'))
	amt_label.grid(row=0,column=0,padx=5,pady=5)
	
	amount=StringVar()
	amt_entry=ttk.Entry(root,width=15,textvariable=amount)
	amt_entry.grid(row=0,column=1,padx=5,pady=5)
	
	sumit_btn=ttk.Button(root,text='Sumit',command=lambda: withdraw_fun(amt_entry.get(),root,acc_no))
	sumit_btn.grid(row=1,columnspan=1,padx=5,pady=5)
	
	root.geometry('450x150+450+200')
	root.mainloop()


def deposit_fun(amt,root,acc_no):
	try:
		amt=float(amt)
	except ValueError:
		mb.showerror('Error','Enter amount should be in integer or floating point manner')
	else:
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		
		cursor.execute(f'update account set T_balance=T_balance+{amt} where ac_no={acc_no}')
		
		cursor.execute(f'select ac_no,Name,T_balance from account where ac_no={acc_no}')
		c=cursor.fetchall()
		
		update_trans_deposit(c[0],amt)
		
		mb.showinfo('Info',f'Amount will be successfully Deposit \n A/c:-{hidden.hide(c[0][0])}\n Name:-{c[0][1]}\n withdrawed amt:-{amt}\n T.amount:-{c[0][2]}')
		#root.destroy()
		
		con.commit()
		con.close()
	
		
	root.destroy()
	
	
def deposit(acc_no):
	root=Tk()
	root.title('Deposit')
	
	amt_label=ttk.Label(root,text='Enter the Deposit amount:-',font=('',15,'bold'))
	amt_label.grid(row=0,column=0,padx=5,pady=5)
	
	amount=IntVar()
	amt_entry=ttk.Entry(root,width=15,textvariable=amount)
	amt_entry.grid(row=0,column=1,padx=5,pady=5)
	
	sumit_btn=ttk.Button(root,text='Sumit',command=lambda: deposit_fun(amt_entry.get(),root,acc_no))
	sumit_btn.grid(row=1,columnspan=1,padx=5,pady=5)
	
	root.geometry('450x150+450+200')
	root.mainloop()
	
def Trans_money_fun2(otp,Enter_otp,root,amt,send_acc_no,acc_no):
	root.destroy()
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	#print(otp)
	#print(Enter_otp)
	#print(Enter_otp==otp)
	#print(Enter_otp!=otp)
	if otp!=Enter_otp:#check why its show true
	
		cursor.execute(f'update account set T_balance=T_balance+{amt} where ac_no={send_acc_no}')
		cursor.execute(f'update account set T_balance=T_balance-{amt} where ac_no={acc_no}')
		#sms.send_sms_notfy()#sms function for notefication
		mb.showinfo('Info','Money successfully Trasffer')
		
		update_trans(amt,acc_no)#update details
		update_trans_to(amt,send_acc_no)
		
		cursor.execute(f'select phone_no from account where ac_no={acc_no}')
		a=cursor.fetchall()
		cursor.execute(f'select phone_no from account where ac_no={send_acc_no}')
		b=cursor.fetchall()
		sms.send_sms_notfy(a[0][0],b[0][0],amt)
		#print(f'{a[0][0]}\n{b[0][0]}')
		
		con.commit()
		
	else:
		mb.showerror('Error','Wrong OTP')
	con.close()
	
def Trans_money_fun1(root,acc_no,send_acc_no,amt):
	root.destroy()
	try:
		amt=float(amt)
		send_acc_no=int(send_acc_no)
	except ValueError:
		mb.showerror('Error','1)Amount should be in integer or floating point \n2)And your entered Account number should be in integer')
	else:
		
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		cursor.execute(f'select * from account where ac_no={send_acc_no}')
		if(cursor.rowcount!=0):
			cursor.execute(f'select phone_no from account where ac_no={acc_no} and T_balance>{amt}')
			if(cursor.rowcount!=0):
				a=cursor.fetchall()
				ans=mb.askquestion('Confirm','You really want to send money')
				if(ans):
					otp=check_otp(a[0][0])
					print(otp)
					root1=Tk()
					root1.title('OTP verification')
									
					otp_label=ttk.Label(root1,text='Enter the OTP:-')
					otp_label.grid(row=0,column=0,padx=5,pady=5)
					
					otp_var=StringVar()
					otp_entry=ttk.Entry(root1,width=10,textvariable=otp_var)
					otp_entry.grid(row=0,column=1,padx=5,pady=5)
					otp_entry.focus()
					
					otp_btn=ttk.Button(root1,text='Check',command=lambda: Trans_money_fun2(otp,otp_entry.get(),root1,amt,send_acc_no,acc_no))
					otp_btn.grid(row=1,columnspan=1,padx=5,pady=10)
					
					root1.geometry('250x150+550+100')
					root1.mainloop()
					
					
			else:
				mb.showerror('Error','Insuffesent Balance')
			
		else:
			messagebox.showinfo('Info','The Entered account not exist please check again!')
		con.commit()
		con.close()
	
def Trans_money(acc_no):
	root=Tk()
	root.title('Tansffer money')
	
	send_label=ttk.Label(root,text='Enter the A/C no. to send money:-',font=('',15,'bold'))
	send_label.grid(row=0,column=0,padx=5,pady=5)
	
	send_entry=ttk.Entry(root,width=15)
	send_entry.grid(row=0,column=1,padx=5,pady=5)
	send_entry.focus()
	
	amt=ttk.Label(root,text='Enter the Amount:-',font=('',15,'bold'))
	amt.grid(row=1,column=0,padx=5,pady=5)
	
	amt_entry=ttk.Entry(root,width=15)
	amt_entry.grid(row=1,column=1,padx=5,pady=5)
	
	send_btn=ttk.Button(root,text='Send',command=lambda: Trans_money_fun1(root,acc_no,send_entry.get(),amt_entry.get()))
	send_btn.grid(row=2,columnspan=1,padx=5,pady=10)
	
	root.geometry('450x150+450+200')
	root.mainloop()
	
	
		
	
def tran_detail(acc_no):
	
		frame2=Tk()
		
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		cursor.execute(f'select * from account where ac_no={acc_no}')
		list=cursor.fetchall()
		
		
		tree=ttk.Treeview(frame2,column=('A/c no','Name','F_name','Gender','D.O.B','Address','Phone no','E-mail','Password','Total Balance'),show='headings')
		
		scrol_bar=Scrollbar(frame2)
		scrol_bar.pack(side='right',fill='y')
		tree.focus_set()
		
		
		tree.column('#1',width=70,minwidth=50,stretch=NO)
		tree.column('#2',width=120,minwidth=100,stretch=NO)
		tree.column('#3',width=150,minwidth=150,stretch=NO)
		tree.column('#4',width=70,minwidth=50,stretch=NO)
		tree.column('#5',width=100,minwidth=100,stretch=NO)
		tree.column('#6',width=120,minwidth=100,stretch=NO)
		tree.column('#7',width=100,minwidth=100,stretch=NO)
		tree.column('#8',width=140,minwidth=100,stretch=NO)
		tree.column('#9',width=100,minwidth=80,stretch=NO)
		tree.column('#10',width=100,minwidth=100,stretch=NO)
		
		tree.heading('#1',text='A/C no')
		tree.heading('#2',text='Name')
		tree.heading('#3',text='F_name')
		tree.heading('#4',text='Gender')
		tree.heading('#5',text='D.O.B')
		tree.heading('#6',text='Address')
		tree.heading('#7',text='Phone no')		 
		tree.heading('#8',text='E-mail')		 
		tree.heading('#9',text='Password')		
		tree.heading('#10',text='Total Balance')
			
		for i in list:
			
			tree.insert('',END,values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
		
		
		#frame2.pack()
		tree.pack()
		scrol_bar.config(command=tree.yview)
		tree.config(yscrollcommand=scrol_bar.set)
		lab1=ttk.Label(frame2,text='Transaction Details',font=('',25))
		lab1.pack()
		#***********************trans_details***********************************
		
		table_name=str(list[0][1]).replace(' ','')+str(list[0][0])
		cursor.execute(f'select * from  {table_name}')
		list2=cursor.fetchall()
		
		
		tree=ttk.Treeview(frame2,column=('Time','Credit','Debit','Total Amount'),show='headings')
		
		scrol_bar=Scrollbar(frame2)
		scrol_bar.pack(side='right',fill='y')
		tree.focus_set()
		
		
		tree.column('#1',width=250,minwidth=250,stretch=NO)
		tree.column('#2',width=150,minwidth=100,stretch=NO)
		tree.column('#3',width=150,minwidth=150,stretch=NO)
		tree.column('#4',width=200,minwidth=200,stretch=NO)
		
		
		tree.heading('#1',text='Date-Time')
		tree.heading('#2',text='Credit')
		tree.heading('#3',text='Debit')	
		tree.heading('#4',text='Total Balance')
			
		for i in list2:
			
			tree.insert('',END,values=(i[0],i[1],i[2],i[3]))
		
		
		#frame2.pack()
		tree.pack(fill='both',expand=True)
		scrol_bar.config(command=tree.yview)
		tree.config(yscrollcommand=scrol_bar.set)
		con.close()
		
		#back_btn=ttk.Button(frame2,text='Back',command=back)
		#back_btn.pack()
	



#************************************customer start page*******************************************
def customer(ac_list):
	root=Tk()
	root.title(ac_list[1])
	frame1=Frame(root)
	frame1.pack()
	wel_msg=ttk.Label(frame1,text=f'Welcome {ac_list[1]}  ',font=('',20,'bold'))
	wel_msg.grid(row=0,column=0)
	
	
	
	btn1=ttk.Button(frame1,text='Withdraw',command= lambda: withdraw_amt(ac_list[0]))
	btn1.grid(row=2,column=0,padx=5,pady=10,sticky='w')
	
	btn2=ttk.Button(frame1,text='Deposit',command=lambda: deposit(ac_list[0]))
	btn2.grid(row=2,column=1,padx=5,pady=10)
	
	btn3=ttk.Button(frame1,text='Transfer money',command=lambda: Trans_money(ac_list[0]))
	btn3.grid(row=4,column=0,padx=5,pady=10,sticky='w')	
	
	btn4=ttk.Button(frame1,text='Tranjection Details',command=lambda:tran_detail(ac_list[0]))
	btn4.grid(row=4,column=1,padx=5,pady=10)
	
	btn5=ttk.Button(frame1,text='logout',command=lambda: logout(root))
	btn5.grid(row=5,columnspan=2,padx=5,pady=10)
	
	
	root.geometry('450x200+250+100')
	root.mainloop()
	

if(__name__=='__main__'):
	l=(100,'monu')
	customer(l)