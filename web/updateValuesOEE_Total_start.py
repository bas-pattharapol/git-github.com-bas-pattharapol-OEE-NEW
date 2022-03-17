import pyodbc
import json
from datetime import datetime, timedelta

server = "172.30.2.2"
port = 5432
database = "OEE_DB"
username = "sa"
password = "p@ssw0rd"

def update(data):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    sum = cnxn.cursor()
    sum.execute("""
                SELECT SUM(o.PlanDownTime) as PlanDownTime , SUM(o.UnplanDownTime) as UnplanDownTime , SUM(o.PlannedProductionTime) as PlannedProductionTime, 
                SUM(o.RunTime1) as RunTime1 , SUM(o.RunTime2) as RunTime2 , SUM(o.TotalCount) as TotalCount , SUM(o.IdealCount1) as IdealCount1 ,
                SUM(o.IdealCount2) as IdealCount2  , SUM(o.GoodCount) as GoodCount , SUM(o.PostReturn) as PostReturn , SUM(o.FinalGoodCount) as FinalGoodCount
                FROM OEE_DB.dbo.OEEReport o WHERE o.PDOrder = ? 
                """,(data[1],))
    for i in sum:
        PlanDownTime = i[0]
        UnplanDownTime = i[1]
        PlannedProductionTime = i[2]
        RunTime1 = i[3]
        RunTime2 = i[4]
        TotalCount = i[5]
        IdealCount1 = i[6]
        IdealCount2 = i[7]
        GoodCount = i[8]
        PostReturn = i[9]
        FinalGoodCount = i[10]
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        UPDATE = cnxn.cursor()
        UPDATE.execute(""" 
                        UPDATE OEE_DB.dbo.[OEEReport_Total] SET 
                        PlanDownTime = ? ,
                        UnplanDownTime = ?,
                        PlannedProductionTime = ?,
                        RunTime1 = ?,
                        RunTime2 = ?,
                        TotalCount = ?,
                        IdealCount1 = ?,
                        IdealCount2 = ?,
                        GoodCount = ?,
                        PostReturn = ?,
                        FinalGoodCount = ?
                        WHERE PDOrder = ?  
                       """,(PlanDownTime,UnplanDownTime,PlannedProductionTime,RunTime1,
                            RunTime2,TotalCount,IdealCount1,IdealCount2,GoodCount,
                            PostReturn,FinalGoodCount,data[1]))
        cnxn.commit()
        
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        oee05 = cnxn.cursor()
        oee05.execute('SELECT QTY FROM OEE_DB.dbo.[INF_OEE5_V2] WHERE PDOrder = ? ',(data[1],))
        
        for i in oee05:
            qty = i[0]
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
            UPDATE = cnxn.cursor()
            UPDATE.execute(""" 
                            UPDATE OEE_DB.dbo.[OEEReport_Total] 
                            SET PostReturn = ?
                            
                            WHERE PDOrder = ?  
                            """,(qty,data[1]))
        cnxn.commit()
            
    
if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    pd = cnxn.cursor()
    pd.execute('select RecordID,PDOrder from OEE_DB.dbo.[OEEReport_Total]  order by RecordID DESC')
    for i in pd:
        update(i)