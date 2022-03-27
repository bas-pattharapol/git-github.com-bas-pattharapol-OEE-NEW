import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
#port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

def startOEE(m):
    allPlanDownTime = 0
    allUnplanDownTime = 0
    allPlannedProductionTime = 0
    allRunTime1 = 0
    allRunTime2 = 0
    allTotalCount = 0
    allIdealCount1 = 0
    allIdealCount2 = 0
    allGoodCount = 0
    allPostReturn = 0
    allFinalGoodCount = 0
    
    Per_PantDownTime = 0
    Per_UnplanDowntime =0
    Per_Downtime = 0
    Per_PantDownTime2 = 0
    Per_UnplanDowntime2 =0
    Per_Downtime2 = 0
    OEE_A1 = 0
    OEE_A2 = 0
    OEE_P1 = 0
    OEE_P2 = 0
    OEE_Q = 0
    OEE_Q_Final = 0
    OEE1Calculation = 0
    OEE2Calculation = 0
    OEE1FinalCalculation = 0
    OEE2FinalCalculation = 0
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.OEEReport_Total ot WHERE OEE_Q2 IS NOT NULL AND DATENAME(MONTH , PostingDate) = DATENAME(MONTH , ?) AND DATENAME(YEAR , PostingDate) = DATENAME(YEAR , ?) AND MachineID = ? ",('2021-10-05','2021-10-05',m[0]))

    for j in data:
        PlantID = j[1]
        PlantName = j[2]
        MachineID = j[7]
        MachineName = j[8]
        ValidateSpeed = j[9]
        allPlanDownTime += j[10]
        allUnplanDownTime += j[11]
        allPlannedProductionTime  += j[12]
        allRunTime1 += j[13]
        allRunTime2  += j[14]
        allTotalCount  += j[15]
        allIdealCount1  += j[16]
        allIdealCount2  += j[17]
        allGoodCount  += j[18]
        allPostReturn  += j[19]
        allFinalGoodCount  += j[20]
    Per_PantDownTime = allPlanDownTime / allRunTime1
    Per_UnplanDowntime = allUnplanDownTime / allRunTime1
    Per_Downtime = Per_PantDownTime + Per_UnplanDowntime 
    Per_PantDownTime2 = allPlanDownTime / allRunTime2
    Per_UnplanDowntime2 = allUnplanDownTime / allRunTime2
    Per_Downtime2 = Per_PantDownTime2 + Per_UnplanDowntime2
    OEE_A1 = (allRunTime2 - allRunTime1)/allRunTime2
    OEE_A2 = (Per_Downtime - allRunTime1) / Per_Downtime
    OEE_P1 = Per_UnplanDowntime2 / Per_Downtime2
    OEE_P2 = Per_UnplanDowntime2 /allTotalCount
    OEE_Q = allGoodCount / allTotalCount
    OEE_Q_Final = allFinalGoodCount / allTotalCount
    OEE1Calculation = OEE_A1 * OEE_P1 * OEE_Q
    OEE2Calculation = OEE_A2 * OEE_P2 * OEE_Q
    OEE1FinalCalculation = OEE_A1 * OEE_P1 * OEE_Q_Final
    OEE2FinalCalculation = OEE_A2 * OEE_P2 * OEE_Q_Final

    print("MachineID : " +str(MachineID))
    print("allPlanDownTime : " + str(allPlanDownTime))  
    print("allUnplanDownTime : " + str(allUnplanDownTime))    
    print("allPlannedProductionTime : " + str(allPlannedProductionTime) )   
    print("allRunTime1 : " + str(allRunTime1))    
    print("allRunTime2 : " + str(allRunTime2)  )  
    print("allTotalCount : " + str(allTotalCount)  )  
    print("allIdealCount1 : " + str(allIdealCount1)  )  
    print("allIdealCount2 : " + str(allIdealCount2)  )  
    print("allGoodCount : " + str(allGoodCount)    )
    print("allPostReturn : " + str(allPostReturn)   ) 
    print("allFinalGoodCount : " + str(allFinalGoodCount)   ) 

    print("Per_PantDownTime : " +str(Per_PantDownTime))
    print("Per_UnplanDowntime : " +str(Per_UnplanDowntime))
    print("Per_Downtime : " +str(Per_Downtime))
    print("Per_PantDownTime2 : " +str(Per_PantDownTime2))
    print("Per_UnplanDowntime2 : " +str(Per_UnplanDowntime2))
    print("Per_Downtime2 : " +str(Per_Downtime2))
    print("OEE_A1 : " +str(OEE_A1))
    print("OEE_A2 : " +str(OEE_A2))
    print("OEE_P1 : " +str(OEE_P1))
    print("OEE_P2 : " +str(OEE_P2))
    print("OEE_Q : " +str(OEE_Q))
    print("OEE_Q_Final : " +str(OEE_Q_Final))
    print("OEE1Calculation : " +str(OEE1Calculation))
    print("OEE2Calculation : " +str(OEE2Calculation))
    print("OEE1FinalCalculation : " +str(OEE1FinalCalculation))
    print("OEE2FinalCalculation : " +str(OEE2FinalCalculation))
            
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    OEEReport_Monthly = cnxn.cursor()
    OEEReport_Monthly.execute("""INSERT INTO OEE_DB.dbo.OEEMonthlyReport (Monthly, PlantID, PlantName, MachineID, MachineName, 
                              PlanDownTime, UnplanDownTime, RunTime1, RunTime2, Per_PantDownTime, 
                              Per_UnplanDowntime, Per_Downtime, Per_PantDownTime2, Per_UnplanDowntime2, Per_Downtime2,
                              TotalCount, IdealCount1, IdealCount2, GoodCount, PostReturn, FinalGoodCount, OEE_A1, OEE_A2, 
                              OEE_P1, OEE_P2, OEE_Q, OEE_Q_Final, OEE1Calculation, OEE2Calculation, 
                              OEE1FinalCalculation, OEE2FinalCalculation) 
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                              ,( 'October 2021'  , PlantID , PlantName  , MachineID  , MachineName  , 
                                allPlanDownTime, allUnplanDownTime, allRunTime1, allRunTime2, 
                                Per_PantDownTime, Per_UnplanDowntime, Per_Downtime, 
                                Per_PantDownTime2, Per_UnplanDowntime2, Per_Downtime2, allTotalCount,
                                allIdealCount1, allIdealCount2, allGoodCount, allPostReturn, allFinalGoodCount,
                                OEE_A1, OEE_A2, OEE_P1, OEE_P2, OEE_Q, OEE_Q_Final, OEE1Calculation,
                                OEE2Calculation, OEE1FinalCalculation, OEE2FinalCalculation ))
    cnxn.commit()  
    
def startYield(m):
    allInputQty = 0
    allOutputQty = 0 
    allReturnQty = 0
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.YieldReport  WHERE FinalYield IS NOT NULL AND DATENAME(MONTH , PostingDate) = DATENAME(MONTH , ?) AND DATENAME(YEAR , PostingDate) = DATENAME(YEAR , ?) AND MachineID = ? ",('2021-10-05','2021-10-05',m[0]))

    for j in data:
        PlantID = j[2]
        PlantName = j[3]
        MachineID = j[8]
        MachineName = j[9]
        allInputQty += j[13]
        allOutputQty += j[14] 
        allReturnQty += j[15]
        
    Yield = allOutputQty / allInputQty
    FinalYield = (allOutputQty - allReturnQty) / allInputQty    
    
    print("allInputQty : " +str(allInputQty))
    print("allOutputQty : " +str(allOutputQty))
    print("allReturnQty : " +str(allReturnQty))
    print("Yield : " +str(Yield))
    print("FinalYield : " + str(FinalYield))  
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    YieldReport_Monthly = cnxn.cursor()
    YieldReport_Monthly.execute('INSERT INTO OEE_DB.dbo.YieldMonthlyReport (Monthly, PlantID, PlantName, MachineID, MachineName, InputQty, OutputQty, ReturnQty, Yield, FinalYield) VALUES(?,?,?,?,?,?,?,?,?,?)' ,( 'October 2021'   , PlantID , PlantName  , MachineID  , MachineName  , allInputQty, allOutputQty, allReturnQty, Yield, FinalYield ))
    cnxn.commit()
    
    print("---------------------------------")
 
def goStart(): 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT DISTINCT MachineID FROM OEE_DB.dbo.OEEReport_Total")

    for i in data :
        startOEE(i)
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT DISTINCT MachineID FROM OEE_DB.dbo.YieldReport")

    for i in data :
        startYield(i)
    
    
    