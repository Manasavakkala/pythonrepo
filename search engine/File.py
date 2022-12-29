import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=HCL-02-72\SQLEXPRESS;'
                    'Database=FileSearchResults;'
                    'TrustedConnection=Yes;')
cursor=conn.cursor()
cursor.execute('''
                INSERT INTO FilesearchResults_table (File_Location,SearchCount,NameOfFile)
                VALUES
                ("C:\Hi\Hello\How\Document.txt"),
                ("C:\sample\sample1\sample2\Tillu.txt")
               ''')
conn.commit();
cursor.execute('Select*From FileSearchResults_table')