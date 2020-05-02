from tkinter import *
from tkinter import ttk
from pymysql import *
import random
from check import check_pass
from tkinter import messagebox as mb
from starting import *
from customer import *



def specific_data_fun(ac,frame1,root):
		frame1.destroy()
		
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		cursor.execute(f'select * from account where ac_no={ac}')
		list=cursor.fetchall()
		
		
		tree=ttk.Treeview(root,column=('A/c no','Name','F_name','Gender','D.O.B','Address','Phone no','E-mail','Password','Total Balance'),show='headings')
		
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
		
		tree.pack()
		con.close()
		root.geometry('1100x100+100+80')
		root.mainloop()


def specific_data():
	#root.destroy()
	
	root=Tk()
	root.title('specific Data')
	
	root1=ttk.Frame(root)
	 
	ac_label=ttk.Label(root1,text='Enter the A/C number:-',font=('',15,'bold'))
	ac_label.grid(row=0,column=0,padx=5,pady=5)
	
	check_ac=StringVar()
	ac_entry=ttk.Entry(root1,width=10,textvariable=check_ac)
	ac_entry.grid(row=0,column=1,padx=5,pady=5)
	ac_entry.focus()
	
	btn1=ttk.Button(root1,text='Sumit',command=lambda: specific_data_fun(ac_entry.get(),root1,root))
	btn1.grid(row=1,columnspan=1,padx=5,pady=10)
	root1.pack()
	
	root.geometry('450x100+250+100')
	root.mainloop()


def delete_data_fun(root,acc):
	
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	
	ans=mb.askquestion('conform','You real want to delete a/c:-')
	
	if(ans=='yes'):
		cursor.execute(f'delete from account where ac_no={acc}')
		con.commit()
		mb.showinfo('Info','A/C successfully Deleted')

	con.commit()
	con.close()	
	root.destroy()
	


def delete_data():
	
	root=Tk()
	root.title('Deleting Data')
	
	del_acc_no=ttk.Label(root,text='Enter the account number:-',font=('',15,'bold'))
	del_acc_no.grid(row=0,column=0,padx=5,pady=5)
	
	del_acc_entry=ttk.Entry(root,width=20)
	del_acc_entry.grid(row=0,column=1,padx=5,pady=5)
	del_acc_entry.focus()
	
	del_btn=ttk.Button(root,text='Delete',command=lambda: delete_data_fun(root,del_acc_entry.get()))
	del_btn.grid(row=1,columnspan=1,padx=5,pady=10)
	
	root.geometry('450x150+250+100')
	root.mainloop()

def logout_admin(root):
	root.destroy()
	import starting as st
	st.start()	

		
def admin_access(name):
	import modules
	root=Tk()
	root.title('Admin')
	root.geometry('500x150+250+100')
	#***********************************customer list************************************
	def back():
		root.destroy()
		admin_access(name)
	
	
	def customer_list(old_frame):
		old_frame.destroy()
		root.geometry('1200x300+100+100')
		frame2=ttk.Frame(root)
		
		con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
		cursor=con.cursor()
		cursor.execute('select * from account')
		list=cursor.fetchall()
		
		
		tree=ttk.Treeview(frame2,column=('A/c no','Name','F_name','Gender','D.O.B','Address','Phone no','E-mail','Password','Total Balance'),show='headings')
		
		scroll1_bar=Scrollbar(frame2)
		scroll1_bar.pack(side='right',fill='y')
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
		
		
		frame2.pack()
		tree.pack(fill='both',expand=True)
		scroll1_bar.config(command=tree.yview)
		tree.config(yscrollcommand=scroll1_bar.set)
		
		con.close()
		
		back_btn=ttk.Button(frame2,text='Back',command=back)
		back_btn.pack()
		#admin_access(name)
	
	
	#/***********************************Admin front page********************************
	frame1=ttk.Frame(root)
	frame1.pack()
	wel_msg=ttk.Label(frame1,text=f'Welcome {name}  ',font=('',20,'bold'))
	wel_msg.grid(row=0,column=0)
	
	
	btn1=ttk.Button(frame1,text='Customer list',command=lambda:customer_list(frame1))
	btn1.grid(row=2,column=0,padx=5,pady=10,sticky='w')
	
	btn2=ttk.Button(frame1,text='Specific Customer Data',command=specific_data)
	btn2.grid(row=2,column=1,padx=5,pady=10)
	
	btn3=ttk.Button(frame1,text='Delete A/C',command=delete_data)
	btn3.grid(row=4,column=0,padx=5,pady=10,sticky='w')	
	
	#btn4=ttk.Button(frame1,text='Modify Data')
	#btn4.grid(row=4,column=1,padx=5,pady=10,sticky='w')
	
	btn5=ttk.Button(frame1,text='logout',command=lambda:logout_admin(root))
	btn5.grid(row=4,column=1,padx=5,pady=10,sticky='w')
	
	
	root.mainloop()
	
if __name__=='__main__':
	admin_access('sir')