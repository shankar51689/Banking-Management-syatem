from pymysql import *
def create_main_tables():
	con=connect(host='localhost',port=3306,user='root',password='monu123',database='bank')
	cursor=con.cursor()
	try:
		cursor.execute('create table IF NOT EXISTS account (ac_no int(20) primary key,Name varchar(20),f_name varchar(30),Gender varchar(7),DOB date,address varchar(50),phone_no bigint(30),E_mail varchar(35),password varchar(15),T_balance decimal(10,5))')
		cursor.execute('create table IF NOT EXISTS admin (Access_id int(10) primary key,Name varchar(20),password varchar(20))')
		cursor.execute("insert IGNORE INTO admin values (1234,'Monu sharma','admin')")
	except Exception:
		pass
		
	if(cursor.fetchall()!=()):
		name='Monu sharma'
		pas='admin'
		cursor.execute(f"insert into admin values(1234,'{name}','{pas}')")
		con.commit()
	con.close()
	
if __name__=='__main__':
	create_main_tables()