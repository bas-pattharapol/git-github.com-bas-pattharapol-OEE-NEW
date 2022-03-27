import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
#port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

def start(m):
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
    
    OEE1FinalCalculation_TLT = 0
    OEE2FinalCalculation_TLT = 0
    OEE1FinalCalculation_HHD = 0
    OEE2FinalCalculation_HHD = 0
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.OEEReport_Total ot WHERE OEE_Q2 IS NOT NULL AND  PostingDate >= DATEADD(year, -1, GETDATE()) ")

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

    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.OEEReport_Total ot WHERE OEE_Q2 IS NOT NULL AND PlantName = 'TLT' AND PostingDate >= DATEADD(year, -1, GETDATE()) ")

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
    OEE1FinalCalculation_TLT = OEE_A1 * OEE_P1 * OEE_Q_Final
    OEE2FinalCalculation_TLT = OEE_A2 * OEE_P2 * OEE_Q_Final
    
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
   
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.OEEReport_Total ot WHERE OEE_Q2 IS NOT NULL AND PlantName = 'HHD' AND PostingDate >= DATEADD(year, -1, GETDATE()) ")

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
        
    try:
        
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
        OEE1FinalCalculation_HHD = OEE_A1 * OEE_P1 * OEE_Q_Final
        OEE2FinalCalculation_HHD = OEE_A2 * OEE_P2 * OEE_Q_Final
    except:
        OEE1FinalCalculation_HHD = 0
        OEE2FinalCalculation_HHD = 0
    
    
    allInputQty = 0
    allOutputQty = 0 
    allReturnQty = 0
    FinalYield = 0
    FinalYield_TLT = 0
    FinalYield_HHD = 0
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.YieldReport  WHERE FinalYield IS NOT NULL AND  PostingDate >= DATEADD(year, -1, GETDATE()) ")
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
    
    allInputQty = 0
    allOutputQty = 0 
    allReturnQty = 0
    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.YieldReport  WHERE FinalYield IS NOT NULL AND PlantName = 'TLT' AND PostingDate >= DATEADD(year, -1, GETDATE()) ")
    for j in data:
        PlantID = j[2]
        PlantName = j[3]
        MachineID = j[8]
        MachineName = j[9]
        allInputQty += j[13]
        allOutputQty += j[14] 
        allReturnQty += j[15]
        
    Yield = allOutputQty / allInputQty
    FinalYield_TLT = (allOutputQty - allReturnQty) / allInputQty   
    
    allInputQty = 0
    allOutputQty = 0 
    allReturnQty = 0
   
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT  * FROM OEE_DB.dbo.YieldReport  WHERE FinalYield IS NOT NULL AND PlantName = 'HHD' AND PostingDate >= DATEADD(year, -1, GETDATE()) ")
    for j in data:
        PlantID = j[2]
        PlantName = j[3]
        MachineID = j[8]
        MachineName = j[9]
        allInputQty += j[13]
        allOutputQty += j[14] 
        allReturnQty += j[15]
    try:    
        Yield = allOutputQty / allInputQty
        FinalYield_HHD = (allOutputQty - allReturnQty) / allInputQty  
    except:
        FinalYield_HHD = 0
        
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    OEEReport_Monthly = cnxn.cursor()
    OEEReport_Monthly.execute('DELETE FROM OEE_DB.dbo.dashboard_METRICS')
    cnxn.commit()  
    
            
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    OEEReport_Monthly = cnxn.cursor()
    OEEReport_Monthly.execute("""INSERT INTO OEE_DB.dbo.dashboard_METRICS
                              (HHD_OEE1,TLT_OEE1,Total_OEE1,
                              HHD_OEE2,TLT_OEE2,Total_OEE2,
                              HHD_Yield,TLT_Yield,Total_Yield)
                              VALUES(?,?,?,?,?,?,?,?,?)"""
                              ,(OEE1FinalCalculation_HHD, OEE1FinalCalculation_TLT,OEE1FinalCalculation,
                                OEE2FinalCalculation_HHD, OEE2FinalCalculation_TLT,OEE2FinalCalculation,
                                FinalYield_HHD,FinalYield_TLT,FinalYield))
    cnxn.commit()  
    

def goStart():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    data = cnxn.cursor()
    data.execute("SELECT DISTINCT MachineID FROM OEE_DB.dbo.OEEReport_Total")

    for i in data :
        start(i)
        

   