from calendar import c
import pyodbc


def ConnectToDB(cursor):
    con= pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='MSI',database='LibraryDatabase',Trusted_Connection='yes')

    cursor=con.cursor()

    

def PrintDataInBooks():
    cursor.execute("SELECT * FROM books")

    for row in cursor:
        print(row)

def PrintDataInStudents():
    cursor.execute("SELECT * FROM students")

    for row in cursor:
        print(row)


def CreateTables():
    cursor.execute("use LibraryDatabase")
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='books' and xtype='U') CREATE TABLE books (bookid INTEGER PRIMARY KEY,name varchar(50) not null,pagecount INTEGER,authorid integer,typeid integer)")
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='borrows' and xtype='U') CREATE TABLE borrows (borrowid integer primary key,studentid integer not null,bookid integer not null,takenDate date,broughtDate date)")
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='students' and xtype='U') CREATE TABLE students (studentid integer primary key,name varchar(50) not null,gender varchar(7),class varchar(50))")
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='authors' and xtype='U') CREATE TABLE authors (authorid integer primary key,name varchar(50) not null)")
    cursor.execute("IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='types' and xtype='U') CREATE TABLE types (typeid integer primary key,name varchar(50) not null)")
    cursor.commit()

def InsertTestDatatoTables():
    cursor.execute("use LibraryDatabase")
    cursor.execute("INSERT INTO books (bookid,name,pagecount,authorid,typeid) values (2,'book1',50,1,1)")
    cursor.commit()


def AddBook(bookid,name,pagecount,authorid,typeid):
    
    insertString=f'INSERT INTO books (bookid,name,pagecount,authorid,typeid) VALUES ({bookid},\'{name}\',{pagecount},{authorid},{typeid})'
    #insertString='INSERT INTO books (bookid,name,pagecount,authorid,typeid) values (%d,%s,%d,%d,%d)'%(bookid,name,pagecount,authorid,typeid)
    #print(insertString)
    cursor.execute(insertString)
    cursor.commit()
    # print("inserted into books table")



def AddStudent(studentid,name,gender,sclass):
    insertString=f'INSERT INTO students (studentid,name,gender,class) VALUES ({studentid},\'{name}\',\'{gender}\',\'{sclass}\')'
    #insertString='INSERT INTO books (bookid,name,pagecount,authorid,typeid) values (%d,%s,%d,%d,%d)'%(bookid,name,pagecount,authorid,typeid)
    #print(insertString)
    cursor.execute(insertString)
    cursor.commit()
    # print("inserted into Student table")



def AddBorrow(borrowid,studentid,bookid,takenDate,broughtDate):
    insertString=f'INSERT INTO borrows (borrowid,studentid,bookid,takenDate,broughtDate) VALUES ({borrowid},{studentid},{bookid},\'{takenDate}\',\'{broughtDate}\')'
    print(insertString)
    cursor.execute(insertString)
    cursor.commit()
    print("inserted into borrows table")


def AddType(typeid,name):
    insertString=f'INSERT INTO types (typeid,name) VALUES ({typeid},\'{name}\')'
    print(insertString)
    cursor.execute(insertString)
    cursor.commit()
    print("inserted into types table")

def AddAurthor(authorid,name):
    insertString=f'INSERT INTO authors (authorid,name) VALUES ({authorid},\'{name}\')'
    print(insertString)
    cursor.execute(insertString)
    cursor.commit()
    print("inserted into authors table")

def FindBook(bookname):
    findString=f'SELECT * FROM books WHERE name like \'%{bookname}%\''
    #print(findString)
    cursor.execute(findString)
    output=cursor.fetchall()
    # print(output)
    if not output:
        print("No Book Found")
    return output

def DeleteBook(bookid):
    DeleteString=f'DELETE FROM books WHERE bookid = {bookid}'
    cursor.execute(DeleteString)
    cursor.commit()

def DeleteStudent(studentid):
    DeleteString=f'DELETE FROM students WHERE studentid={studentid}'
    cursor.execute(DeleteString)
    cursor.commit()

def DeleteAuthor(authorid):
    DeleteString=f'DELETE FROM authors WHERE authorid={authorid}'
    cursor.execute(DeleteString)
    cursor.commit()
    
def DeleteBorrow(borrowid):
    DeleteString=f'DELETE FROM borrows WHERE borrowid={borrowid}'
    cursor.execute(DeleteString)
    cursor.commit()

def BooksBorrowedByStudent(studentid):
    SearchString=f'SELECT b.name from books b join borrows bo on bo.bookid=b.bookid where studentid={studentid}  '
    cursor.execute(SearchString)
    output=cursor.fetchall()
    # print (output)
    return output

#!------Creatting Connection with DBMS-------
con= pyodbc.connect(driver='ODBC Driver 17 for SQL Server',server='MSI',database='LibraryDatabase',username='MSI\ahmad',Trusted_Connection='yes')
cursor=con.cursor()
#!-------Connection Done--------

CreateTables()
# InsertTestDatatoTables()#! Test done
# AddBook(1,'book1',56,4,5)#!Test done Pass only parameters  and data will be inserted into book tables
# AddStudent(1,'Ahmad Mahmood','Male','BSCS-4')#!Test done Pass only parameters  and data will be inserted into Students tables
# AddBorrow(1,1,3,'3/3/2021','4/4/2021')#!Test done Pass only parameters  and data will be inserted into Borrowa tables
#AddType(1,'type1')#!Test done Pass only parameters  and data will be inserted ito types Tables
# AddAurthor(12,'Ahmad')#!Test done Pass only parameters  and data will be inserted into authors Tables
# output=FindBook('book')#!Test done Pass only parameters and data will be returned in form of string
#print(output)
#DeleteBook(3)#!Test done Pass only parameters and data and it will delete from books table
#DeleteStudent(1)#!Test done Pass only parameters and data will delete in student
#DeleteAuthor(12)#!Test done Pass only parameters and data will delete in author tables only
# DeleteBorrow(1)
BooksBorrowedByStudent(200785)#! will return book name borrowed by student
#PrintDataInBooks()
#PrintDataInStudents()



