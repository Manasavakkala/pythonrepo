import pyodbc
import Employee_schema

server = 'HCL-02-72\SQLEXPRESS'
database = 'Employee'
username = 'Capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class Existing(Exception):
    pass
class Not_in_Range(Exception):
    pass
class Employee:
    bonus=2
    project=['C','Java','Python']
    def __init__(self,NameOfEmployee,Salary,Project):
        self.NameOfEmployee=NameOfEmployee
        self.Salary=Salary
        self.Project=Project
    def insert_values(self):
        query4='''
                  INSERT INTO Employee_table(NameOfEmployee,Salary,Project)
                  VALUES
                  ('{0}',{1},'{2}') 
                  '''
        insert_query3=query4.format(self.NameOfEmployee,self.Salary,self.Project)
        cursor.execute(insert_query3)
        query4=cursor.execute('''select *from Employee_table''')
        cnxn.commit()

    def update_salary(self):
        salary=int(input())
        try:

            if salary!=self.Salary:
                fileinfoquery5='''
                                  update Employee_table SET Salary='{0}' WHERE NameOfEmployee='{1}'
                               '''
                update_query5=fileinfoquery5.format(salary,self.NameOfEmployee)
                cursor.execute(update_query5)
                cursor.commit()

            else:
                raise  Existing
        except  Existing:
            print("No change in salary")
    def changeinproject(self):
        new_project=input()
        if new_project==self.project:
            print("Both are same")
        else:
            fileinfoquery5 = '''
                                              update Employee_table SET Project='{0}' WHERE NameOfEmployee='{1}'
                                           '''
            update_query5 = fileinfoquery5.format(new_project, self.NameOfEmployee)
            cursor.execute(update_query5)
            cursor.commit()

    def displayemployeedetails(self):
        query = ''' select * from Employee_Table where NameOfEmployee = '{0}' '''
        searchQuery = query.format(self.NameOfEmployee)
        values = cursor.execute(searchQuery)
        for fileInfo in values:
            # print("==========================")
            print("name={0},Salary={1},project={2} ".format(fileInfo.NameOfEmployee, fileInfo.Salary,fileInfo.Project))


    def add_bonus(self,currentbonus,NameOfEmployee):
        try:
            self.currentbonus=currentbonus
            self.NameOfEmployee=NameOfEmployee
            if currentbonus <= 2 and currentbonus > 0:
                self.Salary=self.Salary+self.Salary*self.currentbonus
                print(self.Salary)
                #query = ''' select * from Employee_Table WHERE NameOfEmployee = '{0}' '''
                #searchQuery = query.format(self.NameOfEmployee)
                #values = cursor.execute(searchQuery)
                query = ''' Update Employee_Table SET Salary={0} WHERE NameOfEmployee = '{1}' '''
                searchQuery = query.format(self.Salary, NameOfEmployee)
                cursor.execute(searchQuery)
                cnxn.commit()


        except:
            pass

obj=Employee('sony',60000,'C')
obj1=Employee_schema.Employee_schema()
#obj1.Employee()

#obj.insert_values()
#obj.update_salary()
#obj.changeinproject()
#obj.displayemployeedetails()
obj.add_bonus(2,'Sony')



