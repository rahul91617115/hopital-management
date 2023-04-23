import mysql.connector as mc#lets us now make a program for 
#program for company
#while writing this program only god and i myself knew whta i meant but now only the one above.
def show_company(database):
    mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
    c=mydb.cursor()
    c.execute("desc COMPANY")
    for i in c:#these lines will give us the tbale informations
        print(i[0],end="\t\t")
    print() 
    c.execute("select * from COMPANY")
    for i in c:
        for k in i:
            print(k,end="\t\t") 
        print()
def show_product(database):
    mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
    c=mydb.cursor()
    c.execute("desc COMPANY")
    for i in c:#these lines will give us the tbale informations
        print(i[0],end="\t\t")
    print() 
    c.execute("select * from COMPANY")
    for i in c:
        for k in i:
            print(k,end="\t\t") 
        print()

def add_COMPANIES(database):#''' COMPANY(C_ID int(90) primary key,C_NAME varchar(90),C_CONTRACT char(3),C_STARTING_DATE char(90))'''
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute('show tables')
        l=[]
        for i in c:
            for k in i:
                l.append(k)
        try:        
            if 'COMPANY' not in l:#this will append the tables in L which we will use to check whther the table is there or not
                c.execute('create table COMPANY(C_ID int(90) primary key,C_NAME varchar(90),C_CONTRACT char(3),C_STARTING_DATE char(90))')
        except:
            print("thank god i dont need to mzke table for you")
        print('let us insert new companies to the database')
        contract="yes"
        while True:
            try:
                cid=input('enter company id. Press enter to exit ')
                if cid=="":
                    break
                else:
                    cu=input("enter the company name ")
                    co=input("in contract?  ")
                    cp=input('enter the date separated by ddmmyyyy')#we have given char so that even an error will betaken without anyw prob
                    if co==" ":
                        qoo="insert into COMPANY values({},'{}','{}','{}')".format(cid,cu,contract,cp)
                        c.execute(qoo)
                        mydb.commit()
                    else:
                        qpop="insert into COMPANY values({},'{}','{}','{}')".format(cid,cu,co,cp)
                        c.execute(qpop)
                        mydb.commit()
        
            except Exception as e:
                print(e)
                
                mydb.rollback()#we have to roll back otherwise it will be quite messed up
        print("successfully done")
        mydb.close()
        mainMAT(database)
        
    except Exception as e:
        print(e)
def UPDATE_COMPANY(database):
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute("desc COMPANY")
        for i in c:#these lines will give us the tbale informations
            print(i[0],end="\t\t")
        print() 
        c.execute("select * from COMPANY")
        for i in c:
            for k in i:
                print(k,end="\t\t") 
            print()
        print("UPDATE MODE ON")
        while True:#this will be running infinitely thereby reducing the user's misery to count the loops
            try:
                USA=input('enter the name of the column you want to update ')
                Value=input('enter your new value ')
                name=input('enter the Name ')
                qoiry="update  COMPANY set {}='{}' where C_NAME='{}'".format(USA,Value,name)
                c.execute(qoiry)
                mydb.commit()
                exit=input("lets exit? y/n").lower()
                if exit=='y':
                    break
            except Exception as e:
                print(e)
                UPDATE_COMPANY(database)
        print("UPDATE MODE OFF")
        mydb.close()
        mainMAT(database)
    except Exception as e:
        print(e)
        UPDATE_COMPANY(DATABASE)
def delete_COMPANY(database):
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute("desc COMPANY")
        for i in c:#these lines will give us the tbale informations
            print(i[0],end="\t\t")
        print() 
        c.execute("select * from COMPANY")
        for i in c:
            for k in i:
                print(k,end="\t\t") 
            print()
        
        foice=input("delete the table or delete the company details? 1/2")
        if foice=='2':
            uff=input('enter the name of the company you want to delete ')
            quiryi="delete from COMPANY where C_NAME='{}'".format(uff)
            c.execute(quiryi)
            mydb.commit()
            mydb.close()
            mainMAT(database)
        elif foice=='1':
            c.execute('drop table COMPANY')
            mydb.commit()
            mydb.close()
            mainMAT(database)
    except Exception as e:
        print(e)
        delete_COMPANY(database)
        mydb.rollback()
    




#program for the PRODUCT
#PRODUCT(P_ID int(90) primary key,P_NAME varchar(90),P_CONTRACT char(3),P_STARTING_DATE char(90),C_ID int(90),foreign key(C_ID) references PRODUCT(C_ID))'
def add_PRODUCTS(database):#''' PRODUCT(C_ID int(90) primary key,C_NAME varchar(90),C_CONTRACT char(3),C_STARTING_DATE char(90))'''
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute('show tables')
        l=[]
        for i in c:
            for k in i:
                l.append(k)
        try:        
            if 'PRODUCT' not in l:#this will append the tables in L which we will use to check whther the table is there or not
                c.execute('create table PRODUCT(P_ID int(90) primary key,P_NAME varchar(90),QUANTITY int(90),P_PURCHASE_DATE char(90),C_ID int(90),foreign key(C_ID) references COMPANY(C_ID))')
                print('product created')
        except:
            print("oh there really do exist a god")
        print('let us insert new PRODUCT to the database')
        contract="yes"
        while True:
            try:
                cid=input('enter product id. Press enter to exit ')
                if cid=="":
                    break
                else:
                    cu=input("enter the product name ")
                    co=input("QUANTITY ")
                    cp=input('enter the date separated by dd/mm/yyyy')#we have given char so that even an error will betaken without anyw prob
                    pid=input("enter the company id of the product ")
                    
                        
                    qpop="insert into PRODUCT values({},'{}','{}','{}',{})".format(cid,cu,co,cp,pid)
                    c.execute(qpop)
                    mydb.commit()
            except Exception as e:
                print(e)
                add_PRODUCTS(database)
                mydb.rollback()#we have to roll back otherwise it will be quite messed up
        print("successfully done")
        mydb.close()
    except Exception as e:
        print(e)
        add_PRODUCTS(database)
def UPDATE_PRODUCT(database):
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute("desc PRODUCT")
        for i in c:#these lines will give us the tbale informations
            print(i[0],end="\t\t")
        print() 
        c.execute("select * from PRODUCT")
        for i in c:
            for k in i:
                print(k,end="\t\t") 
            print()
        print("UPDATE MODE ON")
        while True:#this will be running infinitely thereby reducing the user's misery to count the loops
            try:
                USA=input('enter the name of the column you want to update ')
                Value=input('enter your new value ')
                name=input('enter the Name ')
                qoiry="update  PRODUCT set {}='{}' where P_NAME='{}'".format(USA,Value,name)
                c.execute(qoiry)
                mydb.commit()
                exit=input("lets exit? y/n").lower()
                if exit=='y':
                    break
            except Exception as e:
                print(e)
                UPDATE_COMPANY(database)
        print("UPDATE MODE OFF")
        mydb.close()
    except Exception as e:
        print(e)
        UPDATE_PRODUCT(database)
def delete_PRODUCT(database):
    try:
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        c.execute("desc PRODUCT")
        for i in c:#these lines will give us the tbale informations
            print(i[0],end="\t\t")
        print() 
        c.execute("select * from PRODUCT")
        for i in c:
            for k in i:
                print(k,end="\t\t") 
            print()
    
        foice=input("delete the table or delete the PRODUCT details? 1/2")
        if foice=='2':
            uff=input('enter the name of the PRODUCT you want to delete ')
            quiryi="delete from PRODUCT where P_NAME='{}'".format(uff)
            c.execute(quiryi)
            mydb.commit()
            mydb.close()
        elif foice=='1':
            c.execute('drop table PRODUCT')
            mydb.commit()
            mydb.close()
    except Exception as e:
        print(e)
        delete_PRODUCT(database)
        mydb.rollback()
def connection_MASKS(database):
    
        mydb=mc.connect(host='localhost',user='root',passwd='mysql',database=database)
        c=mydb.cursor()
        asking=input('you want the information of all the PRODUCT or information of just one prof? 1/2')
        if asking=='1':
            c.execute("select * from COMPANY,PRODUCT where PRODUCT.C_ID=COMPANY.C_ID")
            for i in c:
                for k in i:
                    print(k,end="\t\t") 
                print()
            mydb.close()
        
        elif asking=='2':
            wiff=input('please enter the product name')
            querrys="select * from COMPANY,PRODUCT where PRODUCT.C_ID=COMPANY.C_ID where P_NAME='{}'".format(wiff)
            c.execute(querrys)
            for i in c:
                for k in i:
                    print(k,end="\t\t") 
                print()
            mydb.close()
        else:
            print("wrong command")
            mainMAT(database)
def mainMAT(database):
    try:
        
        print("PURPOSES:\n1)ADD COMPANIES\n2)DELETE COMPANY \n3)UPDATE COMPANIES ")
        print("4)ADD PRODUCT\n5)DELETE PRODUCT \n6)PRODUCT UPDATION")
        print("7)SHOW COMPANIES DETAILS \n 8)SHOW PRODUCTS DETAILS")
        
        mydb=mc.connect(host='localhost',user='root',passwd='mysql')
        c=mydb.cursor()
        c.execute("show databases")
        try:   
            if database not in  c:
                basic="create database {}".format(database)
                c.execute(basic)
        except Exception as e:
            
            basic="use database {}".format(database)
        dusk=int(input('enter the pupose '))
        if dusk==1:
            add_COMPANIES(database)
        elif dusk==2:
            delete_COMPANY(database)
        elif dusk==3:
            UPDATE_COMPANY(database)
        elif dusk==4:
            add_PRODUCTS(database)
        elif dusk==5:
            delete_PRODUCT(database)
        elif dusk==6:
            UPDATE_PRODUCT(database)
        elif dusk==7:
            show_company(database)
        elif duck==8:
            show_product(database)
        else:
            print("not here witch")
            mainMAT(database)
    except Exception as e:
        print(e)



    

