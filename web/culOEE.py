import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
#port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

ValidateSpeed = 0
PlanDownTime = 0
UnplanDownTime = 0
PlannedProductionTime = 0
RunTime1 = 0
TotalCount = 0
GoodCount = 0
PostReturn = 0

def startOEE():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder,PostingDate from OEEReport  order by RecordID DESC')
    for i in pd:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        RecordID = cnxn.cursor()
        RecordID.execute('select * from OEEReport where RecordID = ? ',(i[0],))
        
        for j in RecordID:
            print('i[0]' , i[0])
            pdorder = j[4]
            total_TotalCount = 0
            total_GoodCount = 0
            total_FinalGoodCount = 0
            
            ValidateSpeed = j[9]
            PlanDownTime =  j[10]
            UnplanDownTime =  j[11]
            PlannedProductionTime = j[12]
            RunTime1 =  j[13]
            TotalCount = j[15]
            GoodCount =  j[18]
            PostReturn =  j[19]
            
            RunTime2 = PlannedProductionTime - PlanDownTime
            IdealCount1 = RunTime1 * ValidateSpeed
            IdealCount2 = RunTime2 * ValidateSpeed
            FinalGoodCount = GoodCount - PostReturn
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute('UPDATE OEE_DB.dbo.[OEEReport] SET FinalGoodCount = ?  WHERE  RecordID = ?  ',(FinalGoodCount,i[0]))
            cnxn.commit()
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            total = cnxn.cursor()
            total.execute('select TotalCount , GoodCount , FinalGoodCount from OEEReport where PDOrder = ? ',(pdorder,))
            
            for t in total :
                total_TotalCount += int(t[0])
                total_GoodCount += int(t[1])
                total_FinalGoodCount += int(t[2])
            
            try:
                OEE_A1 = (RunTime1 - UnplanDownTime)/RunTime1
                OEE_A2 = (RunTime2 - UnplanDownTime)/RunTime2
                OEE_P1 = TotalCount / IdealCount1
                OEE_P2 = TotalCount / IdealCount2
                OEE_Q1 = total_GoodCount / total_TotalCount
                OEE_Q1_Final = total_FinalGoodCount / total_TotalCount
                OEE_Q2 = GoodCount / TotalCount
                OEE_Q2_Final = FinalGoodCount / TotalCount
                OEE1Calculation = OEE_A1 * OEE_P1 * OEE_Q1 
                OEE2Calculation = OEE_A2 * OEE_P2 * OEE_Q2 
                OEE1FinalCalculation = OEE_A1 * OEE_P1 * OEE_Q1_Final 
                OEE2FinalCalculation = OEE_A2 * OEE_P2 * OEE_Q2_Final 
            except:
                OEE_A1 = (RunTime1 - UnplanDownTime)/RunTime1
                OEE_A2 = (RunTime2 - UnplanDownTime)/RunTime2
                OEE_P1 = 0
                OEE_P2 = 0
                OEE_Q1 = total_GoodCount / total_TotalCount
                OEE_Q1_Final = total_FinalGoodCount / total_TotalCount
                OEE_Q2 = 0
                OEE_Q2_Final = 0
                OEE1Calculation = OEE_A1 * OEE_P1 * OEE_Q1 
                OEE2Calculation = OEE_A2 * OEE_P2 * OEE_Q2 
                OEE1FinalCalculation = OEE_A1 * OEE_P1 * OEE_Q1_Final 
                OEE2FinalCalculation = OEE_A2 * OEE_P2 * OEE_Q2_Final 

        
            print('RunTime2' , RunTime2)
            print('IdealCount1' , IdealCount1)
            print('IdealCount2' , IdealCount2)
            print('FinalGoodCount' , FinalGoodCount)
            
            print('OEE_A1 ', OEE_A1)
            print('OEE_A2 ', OEE_A2)
            print('OEE_P1 ', OEE_P1)
            print('OEE_P2 ', OEE_P2)
            print('OEE_Q1 ', OEE_Q1)
            print('OEE_Q1_Final ', OEE_Q1_Final)
            print('OEE_Q2 ', OEE_Q2)
            print('OEE_Q2_Final ', OEE_Q2_Final)
            print('OEE1Calculation ', OEE1Calculation)
            print('OEE2Calculation ', OEE2Calculation)
            print('OEE1FinalCalculation ', OEE1FinalCalculation)
            print('OEE2FinalCalculation ', OEE2FinalCalculation)
            
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("""UPDATE OEE_DB.dbo.[OEEReport] 
                            SET 
                            RunTime2 = ?,
                            IdealCount1 = ?,
                            IdealCount2 = ?,
                            FinalGoodCount = ?,
                            OEE_A1 = ?,
                            OEE_A2 = ?,
                            OEE_P1 = ?,
                            OEE_P2 = ?,
                            OEE_Q1 = ?,
                            OEE_Q1_Final = ?,
                            OEE_Q2 = ?,
                            OEE_Q2_Final = ?,
                            OEE1Calculation = ?,
                            OEE2Calculation = ?,
                            OEE1FinalCalculation = ?,
                            OEE2FinalCalculation = ?
                            WHERE RecordID = ? """,(
                                RunTime2 ,
                                IdealCount1, 
                                IdealCount2,
                                FinalGoodCount ,
                                OEE_A1 ,
                                OEE_A2 ,
                                OEE_P1 ,
                                OEE_P2 ,
                                OEE_Q1 ,
                                OEE_Q1_Final,
                                OEE_Q2 ,
                                OEE_Q2_Final ,
                                OEE1Calculation ,
                                OEE2Calculation ,
                                OEE1FinalCalculation,
                                OEE2FinalCalculation,
                                i[0]))
            cnxn.commit()

def startYield():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select PDOrder from OEE_DB.dbo.[YieldReport] ')
    
    for i in pd:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        data = cnxn.cursor()
        data.execute('select * from OEE_DB.dbo.[YieldReport] WHERE PDOrder = ? ',(i[0]))
        
        for j in data:
            InputQty = j[13]
            OutputQty = j[14]
            ReturnQty = j[15]
            
            Yield = (OutputQty / InputQty) 
            FinalYield =( (OutputQty - ReturnQty) / InputQty) 
            print('Yield' , Yield)
            print('FinalYield' , FinalYield)
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute("UPDATE OEE_DB.dbo.[YieldReport] SET Yield = ? , FinalYield = ? WHERE PDOrder = ?  ",(Yield,FinalYield,i[0]))
            cnxn.commit()


            