from pymysql import *
from datetime import datetime

def create_table_details(name,ac):
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	
	table_name=str(name).replace(' ','')+str(ac)
	try:
		cursor.execute(f'create table IF NOT EXISTS {table_name} (Time varchar(45) ,credit  bigint(50), Debit bigint(50),Total_Amount bigint(50) )')
		a=cursor.fetchall()
		#print(a)
		con.commit()
		con.close()
	except Exception():
		return
		con.close()
	

def update_trans_withdraw(cus_list,amt):
	table_name=str(cus_list[1]).replace(' ','')+str(cus_list[0])  #name+ac
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	today=datetime.now()
	create_table_details(cus_list[1],cus_list[0])
	cursor.execute(f"insert into {table_name} values('{today}',{amt},0,{cus_list[2]})")
	con.commit()
	con.close()
	


def update_trans_deposit(cus_list,amt):
	table_name=str(cus_list[1]).replace(' ','')+str(cus_list[0])  #name+ac
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	today=datetime.now()
	create_table_details(cus_list[1],cus_list[0])
	cursor.execute(f"insert into {table_name} values('{today}',0,{amt},{cus_list[2]})")
	
	con.commit()
	con.close()
	

def update_trans(amt,ac):
	 
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	cursor.execute(f'select ac_no,Name,T_balance from account where ac_no={ac}')
	c=cursor.fetchall()
	update_trans_withdraw(c[0],amt)
	con.close()
	
def update_trans_to(amount,account):
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	cursor.execute(f"select * from account where ac_no={account}")
	a=cursor.fetchall()
	create_table_details(a[0][1],a[0][0])
	l=(a[0][0],a[0][1],a[0][9])
	update_trans_deposit(l,amount)
	
if __name__=='__main__':
	create_table_details('Monu sharma',1001)