import pyodbc

server = 'HCL-02-72\SQLEXPRESS'
database = 'Employee'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class exits(Exception):
    pass
class Employee_schema:
    def Employee(self):
        try:
            values=cursor.execute('''select *from Employee_table''')
            if(not(values)):
                query1=cursor.execute('''use Employee''')
                query2=cursor.execute('''create table Employee_table
                                (
                                NameOfEmployee Varchar(50),
                                Salary int,
                                Project Varchar(50)
                                )
                                ''')
                query3=cursor.execute('''select *from Employee_table''')
                cnxn.commit()
            else:
                raise exits
        except exits:
            print("table exits")
#obj=Employee_schema()
#obj.Employee()
