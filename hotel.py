import datetime
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="userName",passwd="passWord", database="hotel")
cur=mycon.cursor()


def tables():
    print('+=========+=========+=========+=========+=========+=========+\n')
    customer="create table if not exists customer(custid int primary key not null auto_increment,fname varchar(20),lname varchar(20),age int(5),address varchar(50),mno bigint(15),checkin datetime,checkout datetime,country varchar(30));"
    cur.execute(customer)
    room="create table if not exists room(rid int primary key not null auto_increment,rtype varchar(30),bed varchar(30),custid int,status varchar(20),price int,foreign key (custid) references customer(custid));"
    cur.execute(room)
    laundry="create table if not exists laundry(clothing varchar(30),price int,lid int primary key not null auto_increment);"
    cur.execute(laundry)
    game="create table if not exists gaming(gid int primary key not null auto_increment,gname varchar(30),gprice int);"
    cur.execute(game)
    store="create table if not exists store(sid int primary key not null auto_increment,wearings varchar(30),price int);"
    cur.execute(store)
    food="create table if not exists restaurant(fid int primary key not null auto_increment,food varchar(30),price int);"
    cur.execute(food)
    mycon.commit()
    print("All Tables Created Successfully\n")
    print('+=========+=========+=========+=========+=========+=========+\n')

def room():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To add new room details, Press -->1\nTo delete Room Details, Press -->2\nTo show Room Details, Press -->3\n')
    enter=int(input('Enter your Choice :-'))
    if enter==1:
        cho="y"
        while cho=="y" or cho=="Y":
            rtyp=input('Enter Room type from: Standard,Deluxe,Joint,Connecting,Suite,Apartment,Accessible:-')
            list=['Standard','Deluxe','Joint','Connecting','Suite','Apartment','Accessible','standard','deluxe','joint','connecting','suite','apartment','accessible']
            listt=['Queen','King','Twin','Hollywood twin','Double-double','queen','king','twin','hollywood twin','double-double']
            if rtyp not in list:
                print('Please select from the given options only\n')
                break
            else:
                bed=input('Enter Bed type from:Queen,King,Twin,Hollywood twin,Double-double:-')
                if bed not in listt:
                    print('Please select from the given options only\n')
                    break
                else:
                    price=int(input('Enter the price of Room:-'))
                    stat='Free'
                    st="insert into room(rtype,bed,price,status) values(%s,%s,%s,%s)"
                    val=(rtyp.title(),bed.title(),price,stat)
                    cur.execute(st,val)
                    mycon.commit()
                    print("Record Inserted\n")
                    cho=input('Insert more Records (Y/N) : ')
                    if cho=="n" or cho=="N":
                        break
                    else:
                        print('Make a valid selection\n')
    elif enter==2:
        query="select * from room"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Rooms ",cur.rowcount)
        a=()
        for x in rec:
            print("Room Id = ", x[0])
            print("Room Type = ", x[1])
            print("Bed Type = ", x[2])
            print("Customer Id = ", x[3])
            print("Status = ", x[4])
            print("Price per day = ", x[5]) 
            print('********************')
        cid=int(input('Enter Room ID to be Deleted :- '))
        delete="delete from room where rid=%s;"
        val=(cid,)
        cur.execute(delete,val)
        mycon.commit()
        print("Item Deleted Succesfully\n")
    elif enter==3:
        query="select * from room"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Room Details: ",cur.rowcount)
        print("\n Printing each row")
        for x in rec:
            print("Room Id = ", x[0])
            print("Room Type = ", x[1])
            print("Bed Type = ", x[2])
            print("Customer Id = ", x[3])
            print("Status = ", x[4])
            print("Price per day = ", x[5])
            print('********************\n')
            cur.close()
                
    else:
        print('Enter a Valid Input')
    
    print('+=========+=========+=========+=========+=========+=========+\n') 
                
        
def customer():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To Check In,Press -->1\nTo See Customer Details, Press -->2\n')
    enter=int(input('Enter Your Choice :- '))
    if enter==1:
        cho="y"
        while cho=="Y" or cho=="y":
            fnam=input('Enter your First name:-')
            lnam=input('Enter your Last name:-')
            ag=int(input('Enter your age(Should be 18+):-'))
            if ag<=18:
                print('Age should be above 18 years')
                break
            elif ag>=130:
                print('Age is beyond Life expectancy!')
                break
            else:
                contry=input('Enter your Country name:- ')
                addr=input('Enter your Address:-')
                mno=int(input('Enter your Phone number:-'))
                if 1000000000>mno>9999999999:
                    print('Please enter a valid Number')
                    break
                else:
                    ckin=datetime.datetime.now()
                    st="insert into customer(fname,lname,age,address,mno,checkin,country) values(%s,%s,%s,%s,%s,%s,%s)"
                    val=(fnam.capitalize(),lnam.capitalize(),ag,addr.title(),mno,ckin,contry.title())
                    cur.execute(st,val)
                    mycon.commit()
                    print("Record Inserted\n")
                cho=input('Insert more Records (Y/N) : ')
                if cho=="n" or cho=="N":
                    break
                else:
                    print('Make a valid selection\n')
    elif enter==2:
        sql_select_Query = "select * from customer"
        cur.execute(sql_select_Query)
        records = cur.fetchall()
        print("\nTotal number of rows in Customer Details: ", cur.rowcount)
        print("\nPrinting each row \n")
        for row in records:
            print("Id = ", row[0], )
            print("First Name = ", row[1])
            print("Last Name = ", row[2])
            print("Age = ", row[3])
            print("Country =", row[8])
            print("Address = ", row[4])
            print("Mobile Number = ", row[5])
            print("Check in = ",row[6])
            print("Check out = ",row[7])
            print('********************')
            cur.close()
    else:
        print('Enter a Valid Option')
   
    print('+=========+=========+=========+=========+=========+=========+\n')
            
def book_room():
    print('+=========+=========+=========+=========+=========+=========+\n')  
    query="select * from room where status='Free'"
    cur.execute(query)
    rec=cur.fetchall()
    print("Total number of rows in Room Details: ",cur.rowcount)
    print("\n Rooms available row")
    for x in rec:
        print("Room Id = ", x[0])
        print("Room Type = ", x[1])
        print("Bed Type = ", x[2])
        print("Status = ", x[4])
        print("Price per day = ", x[5])
        print('********************')
    l=int(input('Enter Room Id to be booked '))
    if l==x[0]:
        ll=int(input('Number of days to be booked '))
        cust=int(input('Enter your Customer Id = '))
        pr="select price from room where rid=%s;"
        val=(l,)
        cur.execute(pr,val)
        print("Total amount to be paid = Rs.",cur.fetchall()[0][0]*ll)
        alter="update room set custid=%s,status='Occupied' where rid=%s;"
        vall=(cust,l)
        cur.execute(alter,vall)
        mycon.commit()
        print('Room Booked Successfully')
    else:
        print('Room ID not found')
    print('+=========+=========+=========+=========+=========+=========+\n')  
    
def checkout():
    print('+=========+=========+=========+=========+=========+=========+\n')
    sql_select_Query = "select * from customer"
    cur.execute(sql_select_Query)
    records = cur.fetchall()
    print("\nTotal number of rows in Customer Details: ", cur.rowcount)
    print("\nPrinting each row \n")
    for row in records:
        print("Id = ", row[0], )
        print("First Name = ", row[1])
        print("Last Name = ", row[2])
        print("Age = ", row[3])
        print("Country =", row[8])
        print("Address = ", row[4])
        print("Mobile Number = ", row[5])
        print("Check in = ",row[6])
        print('+=======+========+')
    cid=int(input('Enter your Customer Id = '))
    ckot=datetime.datetime.now()
    up="update customer set checkout=%s where custid=%s;"
    val=(ckot,cid)
    cur.execute(up,val)

    upp="update room set custid=NULL,status='Free' where custid=%s;"
    vall=(cid,)
    cur.execute(upp,vall)
    mycon.commit()
    print("Checked Succesfully\n")
    print('+=========+=========+=========+=========+=========+=========+\n') 
    
def laundry():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To add item, Press -->1\nTodelete item, Press -->2\nTo generate Bill per Item, Press-->3\n') 
    enter=int(input('Enter your Choice :- '))
    if enter==1:
          ch="y"
          while ch=="y" or ch=="Y":
              cloth=input('Enter Cloth name:-')
              prc=int(input('Enter Price:-'))
              st="insert into laundry(clothing,price) values(%s,%s)"
              val=(cloth.title(),prc)
              cur.execute(st,val)
              mycon.commit()
              print('Record Inserted Succesfully')
              ch=input('Enter more records(Y/N)')
    elif enter==2:
        query="select * from laundry"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Laundry ",cur.rowcount)
        a=()
        for x in rec:
            print("L Id = ", x[2])
            print("Cloth = ", x[0])
            print("Price = ", x[1])
            print('********************')
        cid=int(input('Enter Cloth ID to be Deleted :- '))
        delete="delete from laundry where lid=%s;"
        val=(cid,)
        cur.execute(delete,val)
        mycon.commit()
        print("Item Deleted Succesfully\n")
    elif enter==3:
        query="select * from laundry"
        cur.execute(query)
        rec=cur.fetchall()
        if len(rec)==0:
            print('No Records Available in Laundry')
        else:
            query="select * from laundry"
            cur.execute(query)
            rec=cur.fetchall()
            print("Total number of rows in Laundry ",cur.rowcount)
            for x in rec:
                print("L Id = ", x[2])
                print("Cloth = ", x[0])
                print("Price = ", x[1])
                print('********************\n')
            l=int(input("Enter the cloth ID of garment  = "))
            ll=int(input('Quantity = '))
            wash="select sum(price) from laundry where lid=%s"
            val=(l,)
            cur.execute(wash,val)
            print("Total amount to be paid = Rs.",cur.fetchall()[0][0]*ll) 
    else:
        print('Enter a Valid Input')
     
    print('+=========+=========+=========+=========+=========+=========+\n')  
        
def food():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To add item,Press -->1\nTodelete item,Press -->2\nTo Generate Bill, Press -->3\n')  
    enter=int(input('Enter your Choice :- '))
    if enter==1:
        ch="y"
        while ch=="y" or ch=='Y':
            food=input('Enter Food item:-')
            prc=input('Enter Price:-')
            st="insert into restaurant(food,price) values(%s,%s)"
            val=(food.title(),prc)
            cur.execute(st,val)
            mycon.commit()
            print('Record Inserted Succesfully')
            ch=input('Enter more records(Y/N)')
    elif enter==2:
        query="select * from restaurant"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Laundry ",cur.rowcount)
        a=()
        for x in rec:
            print("F ID= ", x[0])
            print("Food Item = ", x[1])
            print("Price = ", x[2])
            print('********************')
        cid=int(input('Enter F ID to be Deleted :- '))
        delete="delete from restaurant where fid=%s;"
        val=(cid,)
        cur.execute(delete,val)
        mycon.commit()
        print("Item Deleted Succesfully")
    elif enter==3:
        query="select * from restaurant"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Restaurant Details: ",cur.rowcount)
        if len(rec)==0:
            print('No Record Available in Restaurant')
        else:
            print("\nDishes available row")
            for x in rec:
                print("Item Id = ", x[0])
                print("Dish = ", x[1])
                print("Price = ", x[2])
                print('********************')
            l=int(input('Enter Item Id to be purchased = '))
            ll=int(input('Quantity = '))
            val=(l,)
            pr="select price from restaurant where fid=%s;"
            cur.execute(pr,val)
            print("Total amount to be paid = Rs.",cur.fetchall()[0][0]*ll)
            mycon.commit()
    else:
        print('Enter a Valid Input\n')
    print('+=========+=========+=========+=========+=========+=========+\n') 
        
def funzone():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To add item,Press -->1\nTo delete item,Press -->2\nTo Generate Bill, Press -->3\n') 
    enter=int(input('Enter your Choice :- '))
    if enter==1:
        ch="y"
        while ch=="y" or ch=='Y':
            name=input('Enter Game name:-')
            prc=input('Enter Price:-')
            st="insert into gaming(gname,gprice) values(%s,%s)"
            val=(name.title(),prc)
            cur.execute(st,val)
            mycon.commit()
            print('Record Inserted Succesfully')
            ch=input('Enter more records(Y/N)')
    elif enter==2:
        query="select * from gaming"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Game Zone ",cur.rowcount)
        a=()
        for x in rec:
            print("G Id = ", x[0])
            print("Game = ", x[1])
            print("Price = ", x[2])
            print('********************')
        cid=int(input('Enter Cloth ID to be Deleted :- '))
        delete="delete from gaming where gid=%s;"
        val=(cid,)
        cur.execute(delete,val)
        mycon.commit()
        print("Item Deleted Succesfully")
    elif enter==3:
        query="select * from gaming"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Fun Zone Details: ",cur.rowcount)
        print("\nGames available row")
        for x in rec:
            print("Game Id = ", x[0])
            print("Game = ", x[1])
            print("Price = ", x[2])
            print('********************')
        l=int(input('Enter Game Id to be purchased = '))
        ll=int(input('Number of Hours to be played = '))
        val=(l,)
        pr="select gprice from gaming where gid=%s;"
        cur.execute(pr,val)
        print("Total amount to be paid = Rs.",cur.fetchall()[0][0]*ll)
        mycon.commit()
    else:
        print('Enter a Valid Input\n')
     
    
    print('+=========+=========+=========+=========+=========+=========+\n')  
        
def store():
    print('+=========+=========+=========+=========+=========+=========+\n')
    print('To add item,Press -->1\nTodelete item,Press -->2\nTo Generate Bill, Press-->3\n') 
    enter=int(input('Enter your Choice :- '))
    if enter==1:
        ch="y"
        while ch=="y":
            name=input('Enter Item name:-')
            prc=input('Enter Price:-')
            st="insert into store(wearings,price) values(%s,%s)"
            val=(name.title(),prc)
            cur.execute(st,val)
            mycon.commit()
            print('Record Inserted Succesfully')
            ch=input('Enter more records(Y/N)')
    elif enter==2:
        query="select * from store"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Store ",cur.rowcount)
        a=()
        for x in rec:
            print("S Id = ", x[0])
            print("Cloth = ", x[1])
            print("Price = ", x[2])
            print('********************')
        cid=int(input('Enter Cloth ID to be Deleted :- '))
        delete="delete from store where sid=%s;"
        val=(cid,)
        cur.execute(delete,val)
        mycon.commit()
        print("Item Deleted Succesfully")
    elif enter==3:
        query="select * from store"
        cur.execute(query)
        rec=cur.fetchall()
        print("Total number of rows in Store Details: ",cur.rowcount)
        print("\nItems available now")
        for x in rec:
            print("Product Id = ", x[0])
            print("Wearing = ", x[1])
            print("Price = ", x[2])
            print('********************\n')
        l=int(input('Enter Produt Id to be purchased = '))
        ll=int(input('Amount = '))
        val=(l,)
        pr="select price from store where sid=%s;"
        cur.execute(pr,val)
        print("Total amount to be paid = Rs.",cur.fetchall()[0][0]*ll)
        mycon.commit()
    else:
        print('Enter a Valid Input')
    print('+=========+=========+=========+=========+=========+=========+\n')




while True:
    cur=mycon.cursor()
    print(" \n +=========+=========+ WELCOME TO HOTEL HILBERT'S +=========+=========+ \n " )
    print('Press the digit corresponding to the activity that you are willing to perform. \n ')
    print('Press ==> (1) CREATE ALL THE TABLES ')
    print('Press ==> (2) CUSTOMERS')
    print('Press ==> (3) ROOMS' )
    print('Press ==> (4) BOOK A ROOM')
    print('Press ==> (5) LAUNDRY ')
    print('Press ==> (6) FOOD COURT')
    print('Press ==> (7) FUN ZONE')
    print('Press ==> (8) SHOPPING AREA')
    print('Press ==> (9) CHECKOUT FROM HOTEL')
    op=int(input("Enter your Choice via corresponding Digit:- "))
    if op==1:
        tables()
    elif op==2:
        customer()
    elif op==3:
        room()
    elif op==4:
        book_room()
    elif op==5:
        laundry()
    elif op==6:
        food()
    elif op==7:
        funzone()
    elif op==8:
        store()
    elif op==9:
        checkout()
    else:
        print("PLEASE MAKE A VALID SELECTION!")