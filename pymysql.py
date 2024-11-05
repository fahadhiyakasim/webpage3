# pip install mysql-connector-python
import mysql.connector
#host,username,password,database
db=mysql.connector.connect(host="localhost",username="root",password="",database="classicmodels") #to make connection
# print(db)
cur=db.cursor() #to get databases
# cur.execute("show databases")
# cur.execute("show tables")
# for i in cur:
#     print(i)
# db.close() #to close execution

# db=mysql.connector.connect(host="localhost",username="root",password="",database="classicmodels")
# cur.execute("create table table2(id int,name varchar(20))")
# cur.execute("show tables")
#cur.execute("show tables")
# for i in cur:
#     print(i)
# db.close() 

# cur.execute("insert into table2(id,name) values(1,'anu')")
# db.commit()
# cur.execute("select * from table2")
# for i in cur:
#     print(i)
# db.close()

# data=(5,"xyz")
# cur.execute("insert into table2 values(%s,%s)",data)
# db.commit()
# print("inserted")
# db.close()

# data=[(6,"xyz"),(7,"asd")]
# cur.executemany("insert into table2 values(%s,%s)",data)
# db.commit()
# print("inserted")
# cur.execute("update table1 set name='xyz' where id=1")
# db.commit()
# cur.execute("delete table1 set name='xyz' where id=1")
# db.commit()
# cur.execute("select * from table2")
# for i in cur:
#     print(i)
# db.close()

