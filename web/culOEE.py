import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.1.2"
port = 5432
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

if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder,PostingDate from OEEReport where OEE1FinalCalculation IS NULL  order by RecordID DESC')
    for i in pd:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        RecordID = cnxn.cursor()
        RecordID.execute('select * from OEEReport where RecordID = ? ',(i[0],))
        
        for j in RecordID:
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
            
            OEE_A1 = (RunTime1 - UnplanDownTime)/RunTime1
            OEE_A2 = (RunTime2 - UnplanDownTime)/RunTime2
            OEE_P1 = TotalCount / IdealCount1
            OEE_P2 = TotalCount / IdealCount2
            OEE_Q1 = GoodCount / TotalCount
            OEE_Q1_Final = FinalGoodCount / TotalCount
            OEE_Q2 = GoodCount / TotalCount
            OEE_Q2_Final = FinalGoodCount / TotalCount
            OEE1Calculation = OEE_A1 * OEE_P1 * OEE_Q1 
            OEE2Calculation = OEE_A1 * OEE_P1 * OEE_Q2 
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

            