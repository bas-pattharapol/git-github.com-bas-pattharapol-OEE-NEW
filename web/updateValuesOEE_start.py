import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.1.2"
port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

def sumV3(pd,ShiftCode,date):
    count = 0
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND ShiftCodeID = ? ",(ShiftCode,))
    
    for i in cur:
        StartTime = str(i[0])      
        EndTime = str(i[1])   
          
        if datetime.strptime(StartTime,'%H:%M:%S') >= datetime.strptime(EndTime,'%H:%M:%S'):
            newdate = datetime.strptime(str(date), '%Y-%m-%d').date() + timedelta(days=1)                      
            
            #print('row.Date',date) 
            #print('newdate',newdate)    
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(newdate) +' ' + EndTime
        else:
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + EndTime
            
    
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE3_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,startDate,endDate))
    
    
    for k in cur:
        count += int(k[0])  
    return count

def sumV4(pd,ShiftCode,date):
    count = 0
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND ShiftCodeID = ? ",(ShiftCode,))
    
    for i in cur:
        StartTime = str(i[0])      
        EndTime = str(i[1])   
          
        if datetime.strptime(StartTime,'%H:%M:%S') >= datetime.strptime(EndTime,'%H:%M:%S'):
            newdate = datetime.strptime(str(date), '%Y-%m-%d').date() + timedelta(days=1)                      
            
            #print('row.Date',date) 
            #print('newdate',newdate)    
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(newdate) +' ' + EndTime
        else:
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + EndTime
            
    
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT QTY FROM OEE_DB.dbo.[INF_OEE4_V2] WHERE PDOrder = ? AND  Time >= ? AND Time <= ? ",(pd,startDate,endDate))

    
    for k in cur:
        count += int(k[0])  
    print('count', count)
    return count

def chTime(pd,ShiftCode,mode,date):
    
    codePlan = []
    codeUnplan = []
    count = 0
    
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    DownTimeCode = conn.cursor()
    DownTimeCode.execute("SELECT Code FROM OEE_DB.dbo.[DownTimeCode] WHERE DeleteFlag = 1 AND Type = 'Plan' ")
    
    for i in DownTimeCode:
        codePlan.append(i[0])
        
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    DownTimeCode = conn.cursor()
    DownTimeCode.execute("SELECT Code FROM OEE_DB.dbo.[DownTimeCode] WHERE DeleteFlag = 1 AND Type = 'Unplan' ")
    
    for i in DownTimeCode:
        codeUnplan.append(i[0])
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT StartTime , EndTime FROM OEE_DB.dbo.[ShiftCode] WHERE DeleteFlag = 1 AND  ShiftCodeID = ? ",(ShiftCode,))
    StartTime = ''
    EndTime = '' 
    for i in cur:
        StartTime = str(i[0])      
        EndTime = str(i[1])   
          
        if datetime.strptime(StartTime,'%H:%M:%S') >= datetime.strptime(EndTime,'%H:%M:%S'):
            newdate = datetime.strptime(str(date), '%Y-%m-%d').date() + timedelta(days=1)                      
            
            print('row.Date',date) 
            print('newdate',newdate)    
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(newdate) +' ' + EndTime
        else:
            startDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + StartTime
            endDate =  str(datetime.strptime(str(date), '%Y-%m-%d').date()) +' ' + EndTime
        
    
    #print('StartTime' , StartTime)
    #print('EndTime' , EndTime)
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = conn.cursor()
    cur.execute("SELECT Min , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' AND StartTime >= ? AND EndTime <= ? ",(pd,startDate,endDate))
    print("SELECT Min , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' AND StartTime >= ? AND EndTime <= ? ",(pd,startDate,endDate))

   
    if mode == 'Plan' :
        for k in cur:
            if k[1] in codePlan:
                print('Plan int(k[0])//60' , int(k[0])//60)
                count += int(k[0])//60
                
    elif mode == 'Unplan':
        for k in cur:
            if k[1] in codeUnplan:
                print('Unplan int(k[0])//60' , int(k[0])//60)
                count += int(k[0])//60
       
    return count

def updateDownTime(pd):
    
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur1 = conn.cursor() 
    cur1.execute("""SELECT TOP(1) iov.MachineID , ppt.PlannedCode from OEE_DB.dbo.INF_OEE1_V2 iov 
                    INNER JOIN OEE_DB.dbo.PlannedProductionTime ppt
                    ON iov.MachineID = ppt.MachineID AND iov.PDOrder = ? AND ppt.[Date] = ? 
                    order by ppt.[DateTime] DESC 
                """,(pd[1] ,pd[2]))
    
    PlanDownTime1 = 0
    UnplanDownTime1 = 0
    PlanDownTime2 = 0
    UnplanDownTime2 = 0
    
    
    for l in cur1 :
        print(l)
        
        if l[1] == 'AA':
            print('1A Plan', chTime(pd[1] ,'1A','Plan',pd[2]))
            print('1A Unplan', chTime(pd[1] ,'1A','Unplan',pd[2]))
            print('2A Plan', chTime(pd[1] ,'2A','Plan',pd[2]))
            print('2A Unplan', chTime(pd[1] ,'2A','Unplan',pd[2]))
            
            PlanDownTime1 = chTime(pd[1] ,'1A','Plan',pd[2])
            UnplanDownTime1 = chTime(pd[1] ,'1A','Unplan',pd[2])
            PlanDownTime2 = chTime(pd[1] ,'2A','Plan',pd[2])
            UnplanDownTime2 = chTime(pd[1] ,'2A','Unplan',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1A' AND PostingDate = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND PostingDate = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,pd[2]))
            cnxn.commit()
            
        elif l[1] == 'BB':
            print('1B Plan', chTime(pd[1] ,'1B','Plan',pd[2]))
            print('1B Unplan', chTime(pd[1] ,'1B','Unplan',pd[2]))
            print('2B Plan', chTime(pd[1] ,'2B','Plan',pd[2]))
            print('2B Unplan', chTime(pd[1] ,'2B','Unplan',pd[2]))
            
            PlanDownTime1 = chTime(pd[1] ,'1B','Plan',pd[2])
            UnplanDownTime1 = chTime(pd[1] ,'1B','Unplan',pd[2])
            PlanDownTime2 = chTime(pd[1] ,'2B','Plan',pd[2])
            UnplanDownTime2 = chTime(pd[1] ,'2B','Unplan',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND PostingDate = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2B' AND PostingDate = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,pd[2]))
            cnxn.commit()
        elif l[1] == 'TOT':  
            print('1OT Plan', chTime(pd[1] ,'1OT','Plan',pd[2]))
            print('1OT Unplan', chTime(pd[1] ,'1OT','Unplan',pd[2]))
            print('2OT Plan', chTime(pd[1] ,'2OT','Plan',pd[2]))
            print('2OT Unplan', chTime(pd[1] ,'2OT','Unplan',pd[2]))
            
            PlanDownTime1 = chTime(pd[1] ,'1OT','Plan',pd[2])
            UnplanDownTime1 = chTime(pd[1] ,'1OT','Unplan',pd[2])
            PlanDownTime2 = chTime(pd[1] ,'2OT','Plan',pd[2])
            UnplanDownTime2 = chTime(pd[1] ,'2OT','Unplan',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1OT' AND PostingDate = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2OT' AND PostingDate = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,pd[2]))
            cnxn.commit()
        elif l[1] == 'HOT': 
            print('1B Plan', chTime(pd[1] ,'1B','Plan',pd[2]))
            print('1B Unplan', chTime(pd[1] ,'1B','Unplan',pd[2]))
            print('2A Plan', chTime(pd[1] ,'2A','Plan',pd[2]))
            print('2A Unplan', chTime(pd[1] ,'2A','Unplan',pd[2]))
            
            PlanDownTime1 = chTime(pd[1] ,'1B','Plan',pd[2])
            UnplanDownTime1 = chTime(pd[1] ,'1B','Unplan',pd[2])
            PlanDownTime2 = chTime(pd[1] ,'2A','Plan',pd[2])
            UnplanDownTime2 = chTime(pd[1] ,'2A','Unplan',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND PostingDate = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND PostingDate = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,pd[2]))
            cnxn.commit()
            
        else:
            print(l[1] ,"Plan" , chTime(pd[1] ,l[1],'Plan',pd[2]))
            print(l[1] ,"Unplan", chTime(pd[1] ,l[1],'Unplan',pd[2]))
            
            PlanDownTime1 = chTime(pd[1] ,l[1],'Plan',pd[2])
            UnplanDownTime1 = chTime(pd[1] ,l[1],'Unplan',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = ? AND PostingDate = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,l[1],pd[2]))
            cnxn.commit()
            
        
        
       

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
            numGoodCount1 = sumV3(pd[1],'1A',pd[2]) + sumV4(pd[1],'1A',pd[2])
            numGoodCount2 = sumV3(pd[1],'2A',pd[2]) + sumV4(pd[1],'2A',pd[2])
            
            print(pd[1],'1A' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1A',pd[2]),pd[1],'1A',pd[2])
            updateRunTime1(sumV3(pd[1],'2A',pd[2]),pd[1],'2A',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1A' AND PostingDate = ?",(numGoodCount1,pd[1],pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND PostingDate = ?",(numGoodCount2,pd[1],pd[2]))
            cnxn.commit()
            
        elif l[1] == 'BB':
            numGoodCount1 = sumV3(pd[1],'1B',pd[2]) + sumV4(pd[1],'1B',pd[2])
            numGoodCount2 = sumV3(pd[1],'2B',pd[2]) + sumV4(pd[1],'2B',pd[2])
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2B' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B',pd[2]),pd[1],'1B',pd[2])
            updateRunTime1(sumV3(pd[1],'2B',pd[2]),pd[1],'2B',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND PostingDate = ?",(numGoodCount1,pd[1],pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2B' AND PostingDate = ?",(numGoodCount2,pd[1],pd[2]))
            cnxn.commit()
        elif l[1] == 'TOT':
            numGoodCount1 = sumV3(pd[1],'1OT',pd[2]) + sumV4(pd[1],'1OT',pd[2])
            numGoodCount2 = sumV3(pd[1],'2OT',pd[2]) + sumV4(pd[1],'2OT',pd[2])
            
            print(pd[1],'1OT' , numGoodCount1)
            print(pd[1],'2OT' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1OT',pd[2]),pd[1],'1OT',pd[2])
            updateRunTime1(sumV3(pd[1],'2OT',pd[2]),pd[1],'2OT',pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1OT' AND PostingDate = ?",(numGoodCount1,pd[1],pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2OT' AND PostingDate = ?",(numGoodCount2,pd[1],pd[2]))
            cnxn.commit()
        elif l[1] == 'HOT':
            numGoodCount1 = sumV3(pd[1],'1B',pd[2]) + sumV4(pd[1],'1B',pd[2])
            numGoodCount2 = sumV3(pd[1],'2A',pd[2]) + sumV4(pd[1],'2A',pd[2])
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B',pd[2]),pd[1],'1B',pd[2],pd[2])
            updateRunTime1(sumV3(pd[1],'2A',pd[2]),pd[1],'2A',pd[2],pd[2])
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND PostingDate = ?",(numGoodCount1,pd[1],pd[2]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND PostingDate = ?",(numGoodCount2,pd[1],pd[2]))
            cnxn.commit()
        else:
            numGoodCount1 = sumV3(pd[1],l[1],pd[2] ) + sumV4(pd[1],l[1],pd[2])
            print(pd[1],l[1] , numGoodCount1)
            
            updateRunTime1(sumV3(pd[1],l[1],pd[2]),pd[1],l[1],pd[2])
           
        
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = ? AND PostingDate = ?",(numGoodCount1,pd[1],l[1],pd[2]))
            cnxn.commit()
            

            
            
def updateRunTime1(sum,pd,ShiftCode,date):
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
        UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET RunTime1 = ? WHERE PDOrder = ? AND ShiftCode = ? AND PostingDate = ? ",(runtime1,pd,ShiftCode,date))
        cnxn.commit()
        

        
if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder,PostingDate from OEEReport order by RecordID DESC')
    for i in pd:
        #updateGoodCount(i)
        updateDownTime(i)