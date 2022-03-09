import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.1.2"
port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

def sumV3(pd,ShiftCode):
    count = 0
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND ShiftCodeID = ? ",(ShiftCode,))
    
    for i in cur:
        StartTime = i[0]      
        EndTime = i[1] 
    if ShiftCode == '1A':
    
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    
    elif ShiftCode == '2A':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND Time >= ? ",(pd,StartTime))
    
    elif ShiftCode == '1B' or ShiftCode == '2B':
    
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    elif ShiftCode == '1OT':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    
    elif ShiftCode == '2OT':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND (Time >= ? OR Time <= ? ) AND (Time <= ? OR Time >= ? ) ",(pd,StartTime,EndTime,EndTime,StartTime))
     
    for k in cur:
        count += int(k[0])  

    return count

def sumV4(pd,ShiftCode):
    count = 0
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND ShiftCodeID = ? ",(ShiftCode,))
    
    for i in cur:
        StartTime = i[0]      
        EndTime = i[1] 
    if ShiftCode == '1A':
    
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    
    elif ShiftCode == '2A':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND Time >= ? ",(pd,StartTime))
    
    elif ShiftCode == '1B' or ShiftCode == '2B':
    
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    elif ShiftCode == '1OT':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND Time >= ? AND Time <= ? ",(pd,StartTime,EndTime))
    
    elif ShiftCode == '2OT':      
          
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND (Time >= ? OR Time <= ? ) AND (Time <= ? OR Time >= ? ) ",(pd,StartTime,EndTime,EndTime,StartTime))
     
    for k in cur:
        count += int(k[0])  
    print('count', count)
    return count

def updateGoodCount(pd):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur1 = conn.cursor()
    cur1.execute(""" SELECT TOP(1) iov.MachineID , ppt.PlannedCode from OEE_DB.dbo.INF_OEE1_V2 iov
                    INNER JOIN OEE_DB.dbo.PlannedProductionTime ppt
                    ON iov.MachineID = ppt.MachineID AND iov.PDOrder = ? AND ppt.[Date] = ? 
                    order by ppt.[DateTime] DESC 
                """,(pd[1] ,pd[2]))
    numGoodCount1 = 0
    numGoodCount2 = 0
    for l in cur1:
        print(l)
        if l[1] == 'AA':
            numGoodCount1 = sumV3(pd[1],'1A') + sumV4(pd[1],'1A')
            numGoodCount2 = sumV3(pd[1],'2A') + sumV4(pd[1],'2A')
            
            print(pd[1],'1A' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1A'),pd[1],'1A')
            updateRunTime1(sumV3(pd[1],'2A'),pd[1],'2A')
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1A'",(numGoodCount1,pd[1]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A'",(numGoodCount2,pd[1]))
            cnxn.commit()
            
        elif l[1] == 'BB':
            numGoodCount1 = sumV3(pd[1],'1B') + sumV4(pd[1],'1B')
            numGoodCount2 = sumV3(pd[1],'2B') + sumV4(pd[1],'2B')
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2B' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B'),pd[1],'1B')
            updateRunTime1(sumV3(pd[1],'2B'),pd[1],'2B')
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B'",(numGoodCount1,pd[1]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2B'",(numGoodCount2,pd[1]))
            cnxn.commit()
        elif l[1] == 'TOT':
            numGoodCount1 = sumV3(pd[1],'1OT') + sumV4(pd[1],'1OT')
            numGoodCount2 = sumV3(pd[1],'2OT') + sumV4(pd[1],'2OT')
            
            print(pd[1],'1OT' , numGoodCount1)
            print(pd[1],'2OT' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1OT'),pd[1],'1OT')
            updateRunTime1(sumV3(pd[1],'2OT'),pd[1],'2OT')
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1OT'",(numGoodCount1,pd[1]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2OT'",(numGoodCount2,pd[1]))
            cnxn.commit()
        elif l[1] == 'HOT':
            numGoodCount1 = sumV3(pd[1],'1B') + sumV4(pd[1],'1B')
            numGoodCount2 = sumV3(pd[1],'2A') + sumV4(pd[1],'2A')
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B'),pd[1],'1B')
            updateRunTime1(sumV3(pd[1],'2A'),pd[1],'2A')
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B'",(numGoodCount1,pd[1]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A'",(numGoodCount2,pd[1]))
            cnxn.commit()
        else:
            numGoodCount1 = sumV3(pd[1],l[1] ) + sumV4(pd[1],l[1])
            print(pd[1],l[1] , numGoodCount1)
            
            updateRunTime1(sumV3(pd[1],l[1]),pd[1],l[1])
           
        
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = ?",(numGoodCount1,pd[1],l[1]))
            cnxn.commit()
            

            
            
def updateRunTime1(sum,pd,ShiftCode):
    runtime1 = 0
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    RunTime1 = cnxn.cursor()
    RunTime1.execute("select ValidateSpeed , SetTime from OEEReport where PDOrder = ? AND ShiftCode = ?",(pd,ShiftCode))
    
    for i in RunTime1:
        print(i,sum)
        runtime1 = round((sum/i[0]) + i[1] , 1)
        
        print('runtime1' , runtime1)
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        UPDATE = cnxn.cursor()
        UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET RunTime1 = ? WHERE PDOrder = ? AND ShiftCode = ?",(runtime1,pd,ShiftCode))
        cnxn.commit()
        

        
if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder,PostingDate from OEEReport where OEE1FinalCalculation IS NULL  order by RecordID DESC')
    for i in pd:
        updateGoodCount(i)