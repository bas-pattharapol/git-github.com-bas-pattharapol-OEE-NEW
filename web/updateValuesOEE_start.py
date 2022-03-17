import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
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
        
    
    print('startDate' , startDate)
    print('endDate' , endDate)

    print("----------------- ",pd,ShiftCode,mode,date,"-----------------------")
   
    try:
        
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("""IF ((SELECT StartTime FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime') >= ? ) AND ((SELECT EndTime FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime') <= ? )
                            SELECT  Min , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' AND StartTime >= ? AND EndTime <= ? 
                        ELSE 
                            IF ((SELECT StartTime FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime') >= ?) AND  ((SELECT EndTime FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime') > ?) 
                                SELECT DATEDIFF(second,StartTime,?) , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' 
                            ELSE 
                                SELECT DATEDIFF(second,?,EndTime) , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' 
                        """
                ,(pd,startDate,pd,endDate,pd,startDate,endDate,
                pd,startDate,pd,endDate,
                endDate,pd,
                startDate,pd))
    except:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cur = conn.cursor()
        cur.execute("SELECT Min , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' AND StartTime >= ? AND EndTime <= ? ",(pd,startDate,endDate))


    # 
    # print("SELECT Min , DownTimeCode FROM OEE_DB.dbo.[INF_OEE2_V2] WHERE PDOrder = ? AND TypeTime = 'DonwTime' AND StartTime >= ? AND EndTime <= ? ",(pd,startDate,endDate))

   
    if mode == 'Plan' :
        for k in cur:
            if k[1] in codePlan:
                print('Plan int(k[0])' , int(k[0]))
                count += int(k[0])
                
    elif mode == 'Unplan':
        for k in cur:
            if k[1] in codeUnplan:
                print('Unplan int(k[0])' , int(k[0]))
                count += int(k[0])
    if count < 0 :
        count = 0
    return count

def updateDownTime(pd):
    ddDate = pd[2].date()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur1 = conn.cursor() 
    cur1.execute("""SELECT TOP(1) iov.MachineID , ppt.PlannedCode from OEE_DB.dbo.INF_OEE1_V2 iov 
                    INNER JOIN OEE_DB.dbo.PlannedProductionTime ppt
                    ON iov.MachineID = ppt.MachineID AND iov.PDOrder = ? AND ppt.[Date] = ? 
                    order by ppt.[DateTime] DESC 
                """,(pd[1] ,ddDate))
    
    PlanDownTime1 = 0
    UnplanDownTime1 = 0
    PlanDownTime2 = 0
    UnplanDownTime2 = 0
    
    
    for l in cur1 :
        print(l)
        
        if l[1] == 'AA':
            print('1A Plan', chTime(pd[1] ,'1A','Plan',ddDate))
            print('1A Unplan', chTime(pd[1] ,'1A','Unplan',ddDate))
            print('2A Plan', chTime(pd[1] ,'2A','Plan',ddDate))
            print('2A Unplan', chTime(pd[1] ,'2A','Unplan',ddDate))
            
            PlanDownTime1 = chTime(pd[1] ,'1A','Plan',ddDate)
            UnplanDownTime1 = chTime(pd[1] ,'1A','Unplan',ddDate)
            PlanDownTime2 = chTime(pd[1] ,'2A','Plan',ddDate)
            UnplanDownTime2 = chTime(pd[1] ,'2A','Unplan',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1A' AND DateTime = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND DateTime = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,ddDate))
            cnxn.commit()
            
        elif l[1] == 'BB':
            print('1B Plan', chTime(pd[1] ,'1B','Plan',ddDate))
            print('1B Unplan', chTime(pd[1] ,'1B','Unplan',ddDate))
            print('2B Plan', chTime(pd[1] ,'2B','Plan',ddDate))
            print('2B Unplan', chTime(pd[1] ,'2B','Unplan',ddDate))
            
            PlanDownTime1 = chTime(pd[1] ,'1B','Plan',ddDate)
            UnplanDownTime1 = chTime(pd[1] ,'1B','Unplan',ddDate)
            PlanDownTime2 = chTime(pd[1] ,'2B','Plan',ddDate)
            UnplanDownTime2 = chTime(pd[1] ,'2B','Unplan',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND DateTime = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2B' AND DateTime = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,ddDate))
            cnxn.commit()
        elif l[1] == 'TOT':  
            print('1OT Plan', chTime(pd[1] ,'1OT','Plan',ddDate))
            print('1OT Unplan', chTime(pd[1] ,'1OT','Unplan',ddDate))
            print('2OT Plan', chTime(pd[1] ,'2OT','Plan',ddDate))
            print('2OT Unplan', chTime(pd[1] ,'2OT','Unplan',ddDate))
            
            PlanDownTime1 = chTime(pd[1] ,'1OT','Plan',ddDate)
            UnplanDownTime1 = chTime(pd[1] ,'1OT','Unplan',ddDate)
            PlanDownTime2 = chTime(pd[1] ,'2OT','Plan',ddDate)
            UnplanDownTime2 = chTime(pd[1] ,'2OT','Unplan',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1OT' AND DateTime = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2OT' AND DateTime = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,ddDate))
            cnxn.commit()
        elif l[1] == 'HOT': 
            print('1B Plan', chTime(pd[1] ,'1B','Plan',ddDate))
            print('1B Unplan', chTime(pd[1] ,'1B','Unplan',ddDate))
            print('2A Plan', chTime(pd[1] ,'2A','Plan',ddDate))
            print('2A Unplan', chTime(pd[1] ,'2A','Unplan',ddDate))
            
            PlanDownTime1 = chTime(pd[1] ,'1B','Plan',ddDate)
            UnplanDownTime1 = chTime(pd[1] ,'1B','Unplan',ddDate)
            PlanDownTime2 = chTime(pd[1] ,'2A','Plan',ddDate)
            UnplanDownTime2 = chTime(pd[1] ,'2A','Unplan',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND DateTime = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND DateTime = ?",(PlanDownTime2,UnplanDownTime2,pd[1] ,ddDate))
            cnxn.commit()
            
        else:
            print(l[1] ,"Plan" , chTime(pd[1] ,l[1],'Plan',ddDate))
            print(l[1] ,"Unplan", chTime(pd[1] ,l[1],'Unplan',ddDate))
            
            PlanDownTime1 = chTime(pd[1] ,l[1],'Plan',ddDate)
            UnplanDownTime1 = chTime(pd[1] ,l[1],'Unplan',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET PlanDownTime = ? ,UnplanDownTime = ? WHERE PDOrder = ? AND ShiftCode = ? AND DateTime = ?",(PlanDownTime1,UnplanDownTime1,pd[1] ,l[1],ddDate))
            cnxn.commit()
            
        
        
       

def updateGoodCount(pd):
    ddDate = pd[2].date()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cur1 = conn.cursor()
    cur1.execute(""" SELECT TOP(1) iov.MachineID , ppt.PlannedCode from OEE_DB.dbo.INF_OEE1_V2 iov
                    INNER JOIN OEE_DB.dbo.PlannedProductionTime ppt
                    ON iov.MachineID = ppt.MachineID AND iov.PDOrder = ? AND ppt.[Date] = ? 
                    order by ppt.[DateTime] DESC 
                """,(pd[1] ,ddDate))
    numGoodCount1 = 0
    numGoodCount2 = 0
    for l in cur1:
        print(l)
        if l[1] == 'AA':
            numGoodCount1 = sumV3(pd[1],'1A',ddDate) + sumV4(pd[1],'1A',ddDate)
            numGoodCount2 = sumV3(pd[1],'2A',ddDate) + sumV4(pd[1],'2A',ddDate)
            
            print(pd[1],'1A' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1A',ddDate),pd[1],'1A',ddDate)
            updateRunTime1(sumV3(pd[1],'2A',ddDate),pd[1],'2A',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1A' AND DateTime = ?",(numGoodCount1,pd[1],ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND DateTime = ?",(numGoodCount2,pd[1],ddDate))
            cnxn.commit()
            
        elif l[1] == 'BB':
            numGoodCount1 = sumV3(pd[1],'1B',ddDate) + sumV4(pd[1],'1B',ddDate)
            numGoodCount2 = sumV3(pd[1],'2B',ddDate) + sumV4(pd[1],'2B',ddDate)
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2B' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B',ddDate),pd[1],'1B',ddDate)
            updateRunTime1(sumV3(pd[1],'2B',ddDate),pd[1],'2B',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND DateTime = ?",(numGoodCount1,pd[1],ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2B' AND DateTime = ?",(numGoodCount2,pd[1],ddDate))
            cnxn.commit()
        elif l[1] == 'TOT':
            numGoodCount1 = sumV3(pd[1],'1OT',ddDate) + sumV4(pd[1],'1OT',ddDate)
            numGoodCount2 = sumV3(pd[1],'2OT',ddDate) + sumV4(pd[1],'2OT',ddDate)
            
            print(pd[1],'1OT' , numGoodCount1)
            print(pd[1],'2OT' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1OT',ddDate),pd[1],'1OT',ddDate)
            updateRunTime1(sumV3(pd[1],'2OT',ddDate),pd[1],'2OT',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1OT' AND DateTime = ?",(numGoodCount1,pd[1],ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2OT' AND DateTime = ?",(numGoodCount2,pd[1],ddDate))
            cnxn.commit()
        elif l[1] == 'HOT':
            numGoodCount1 = sumV3(pd[1],'1B',ddDate) + sumV4(pd[1],'1B',ddDate)
            numGoodCount2 = sumV3(pd[1],'2A',ddDate) + sumV4(pd[1],'2A',ddDate)
            
            print(pd[1],'1B' , numGoodCount1)
            print(pd[1],'2A' , numGoodCount2)
            
            updateRunTime1(sumV3(pd[1],'1B',ddDate),pd[1],'1B',ddDate)
            updateRunTime1(sumV3(pd[1],'2A',ddDate),pd[1],'2A',ddDate)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '1B' AND DateTime = ?",(numGoodCount1,pd[1],ddDate))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = '2A' AND DateTime = ?",(numGoodCount2,pd[1],ddDate))
            cnxn.commit()
        else:
            numGoodCount1 = sumV3(pd[1],l[1],ddDate ) + sumV4(pd[1],l[1],ddDate)
            print(pd[1],l[1] , numGoodCount1)
            
            updateRunTime1(sumV3(pd[1],l[1],ddDate),pd[1],l[1],ddDate)
           
        
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET GoodCount = ? WHERE PDOrder = ? AND ShiftCode = ? AND DateTime = ?",(numGoodCount1,pd[1],l[1],ddDate))
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
        UPDATE.execute("UPDATE OEE_DB.dbo.[OEEReport] SET RunTime1 = ? WHERE PDOrder = ? AND ShiftCode = ? AND DateTime = ? ",(runtime1,pd,ShiftCode,date))
        cnxn.commit()
        
def updateYield(i):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    GoodCount = cnxn.cursor()
    GoodCount.execute("""SELECT sum(o.GoodCount) 
                        FROM  OEE_DB.dbo.OEEReport o 
                        INNER JOIN OEE_DB.dbo.YieldReport y
                        ON o.PDOrder = y.PDOrder AND y.PDOrder = ? AND o.PDOrder = ? """,
                        (i[1],i[1]))
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    ReturnQty = cnxn.cursor()
    ReturnQty.execute('select PDOrder,QTY from OEE_DB.dbo.[INF_OEE5_V2] WHERE PDOrder = ? ',(i[1],))
    
    for p in ReturnQty:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        UPDATE = cnxn.cursor()
        UPDATE.execute("UPDATE OEE_DB.dbo.[YieldReport] SET ReturnQty = ? WHERE PDOrder = ?  ",(p[1],i[1]))
        cnxn.commit()
    
    for p in GoodCount:
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        UPDATE = cnxn.cursor()
        UPDATE.execute("UPDATE OEE_DB.dbo.[YieldReport] SET OutputQty = ? WHERE PDOrder = ?  ",(p[0],i[1]))
        cnxn.commit()
        
if __name__ == '__main__':
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    #pd = cnxn.cursor()
    #pd.execute('select RecordID,PDOrder,DateTime from OEEReport order by RecordID DESC')
    #for i in pd:
    #    updateGoodCount(i)
    #    updateDownTime(i)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder from OEE_DB.dbo.[YieldReport]  order by RecordID DESC')
    for i in pd:
        updateYield(i)