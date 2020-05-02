from pymysql import *
import random
from check import *
from customer import *
from tkinter import *
from tkinter import messagebox as mb
import modules


def login(acc_no,pass_word):
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	
	cursor.execute(f"select * from account where ac_no={acc_no} and Password='{pass_word}'")
	if(cursor.rowcount!=0):
		name=cursor.fetchall()
		return (name,True)
	else:
		return False
		
def new_user(l):
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	if(int(l[4])<10):
		l[4]='0'+l[4]
	if(int(l[5])<10):
		l[5]='0'+l[5]
	
	dob=l[3]+l[4]+l[5]
	dob=int(dob)
	ac_no=random.randint(0000,9999)

	cursor.execute(f"insert into account values({ac_no},'{l[0]}','{l[1]}','{l[2]}',{dob},'{l[6]}',{l[7]},'{l[8]}','{l[9]}',0)")
	mb.showinfo('info',f'your account successfully created\nA/C No:-{ac_no}\nName:-{l[0]},\nTotal Balance:-NIL')
	modules.create_table_details(l[0],ac_no)
	
	
	con.commit()
	con.close()

	
def admin_login(acc,pass_word):
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
		
	cursor.execute(f"select * from admin where Access_id={acc} and password='{pass_word}'")
	
	if(cursor.rowcount!=0):
		name=cursor.fetchall()
		return (True,name[0][1])
	else:
		return False
		
